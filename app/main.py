# app/main.py
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from .database import SessionLocal, init_db
from .models import Report, ReportIn, ReportOut, StatsOut
from .abuse_types import abuse_types
from .translations import translations
from datetime import datetime

app = FastAPI(title="JusticeDigitalMVP")
init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

DEFAULT_LANG = "fr"
def T(lang: str, key: str) -> str:
    return translations.get(lang, translations[DEFAULT_LANG]).get(
        key, translations[DEFAULT_LANG].get(key, "")
    )

@app.get("/abuse-types")
def list_abuse_types(lang: str = Query(DEFAULT_LANG, regex="^(fr|es|en|sw|ln)$")):
    return {"lang": lang, "types": abuse_types[lang]}

@app.post("/reports", response_model=ReportOut)
def create_report(payload: ReportIn, db: Session = Depends(get_db)):
    lang = payload.idioma if payload.idioma in abuse_types else DEFAULT_LANG
    if payload.tipo_abuso not in abuse_types[lang]:
        raise HTTPException(status_code=400, detail=T(lang, "invalid_code"))
    report = Report(
        texto=payload.texto,
        tipo_abuso=payload.tipo_abuso,
        idioma=lang,
        source=payload.source,
    )
    db.add(report); db.commit(); db.refresh(report)
    return {
        "id": report.id,
        "message": T(lang, "report_saved"),
        "idioma": lang,
        "created_at": report.created_at,
    }

@app.get("/stats", response_model=StatsOut)
def stats(lang: str = Query(DEFAULT_LANG, regex="^(fr|es|en|sw|ln)$"), db: Session = Depends(get_db)):
    rows = db.query(Report).all()
    total = len(rows)
    counts = {}
    for r in rows:
        label = abuse_types[lang].get(r.tipo_abuso, abuse_types[lang]["other_abuses"])
        counts[label] = counts.get(label, 0) + 1
    return {"message": T(lang, "stats"), "total": total, "por_tipo": counts}

@app.get("/stats/export")
def stats_export(lang: str = Query(DEFAULT_LANG, regex="^(fr|es|en|sw|ln)$"), db: Session = Depends(get_db)):
    import csv, io
    rows = db.query(Report).all()
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["id", "texto", "tipo_abuso_code", "tipo_abuso_label", "idioma", "created_at"])
    for r in rows:
        writer.writerow([r.id, r.texto, r.tipo_abuso, abuse_types[lang].get(r.tipo_abuso, ""), r.idioma, r.created_at.isoformat()])
    return {"lang": lang, "csv": buffer.getvalue()}
# app/main.py (suite)
from pydantic import BaseModel
from .ai import classify_question
from .abuse_types import abuse_types

class Consulta(BaseModel):
    user: str
    question: str
    lang: str = DEFAULT_LANG

@app.post("/consultation")
def consultation(data: Consulta):
    lang = data.lang if data.lang in abuse_types else DEFAULT_LANG
    label, score = classify_question(data.question)

    if label and label in abuse_types[lang]:
        return {
            "message": T(lang, "success"),
            "interpretation": f"{abuse_types[lang][label]}",
            "confidence": f"{score:.2f}",
            "suggestion": f"Créer une dénonciation avec le code '{label}' via /reports",
            "disclaimer": "Cette consultation est informative et ne remplace pas un avocat."
        }

    # Fallback simple par recherche de sous-chaînes
    q = data.question.lower()
    detected = None
    for code, label_local in abuse_types[lang].items():
        if label_local.lower() in q:
            detected = (code, label_local)
            break

    if detected:
        code, label_local = detected
        return {
            "message": T(lang, "success"),
            "interpretation": label_local,
            "confidence": "0.50",
            "suggestion": f"Créer une dénonciation avec le code '{code}' via /reports",
            "disclaimer": "Cette consultation est informative et ne remplace pas un avocat."
        }

    return {
        "message": T(lang, "success"),
        "interpretation": "Question générale",
        "confidence": "0.00",
        "suggestion": "Consulter /abuse-types ou /stats",
        "disclaimer": "Cette consultation est informative et ne remplace pas un avocat."
    }
# app/main.py (extraits à ajouter)
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import datetime
from pydantic import BaseModel

from .audit import AbuseReport, log_declaration, log_classification, audit_logger, GOVERNANCE
from .abuse_types import abuse_types
from .database import SessionLocal, init_db
# ... autres imports

app = FastAPI(title="LexCivic API")
init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint de création de report (avec audit)
@app.post("/reports/audited")
def create_report_audited(data: AbuseReport, db: Session = Depends(get_db)):
    lang = data.language if data.language in abuse_types else "fr"

    # Validation taxonomique minimale
    # si category format code ex: COR-001 => ok, sinon mapping libre si "abuse_of_power"... adapter selon besoin
    # Ici, on accepte code interne ou clé de taxonomie existante
    code_ok = (
        data.category in abuse_types.get(lang, {}) or
        isinstance(data.category, str)
    )
    if not code_ok:
        raise HTTPException(status_code=400, detail="Code de catégorie invalide")

    # Sauvegarde (ex: table Report) - à adapter à ton modèle
    # db.add(...); db.commit()

    # Audit: log la déclaration (received -> validated si DB OK)
    log_declaration(data, status="validated")
    return {"message": "Déclaration enregistrée et auditée", "lang": lang}

# Endpoint d’audit: exporter les logs
@app.get("/audit/logs")
def audit_logs(format: str = Query("json", regex="^(json|yaml)$")):
    if format == "json":
        payload = audit_logger.export_json()
        log_export("json", user="system")
        return {"format": "json", "logs": payload}
    else:
        try:
            payload = audit_logger.export_yaml()
            log_export("yaml", user="system")
            return {"format": "yaml", "logs": payload}
        except RuntimeError as e:
            raise HTTPException(status_code=500, detail=str(e))

# Endpoint: schéma de gouvernance
@app.get("/audit/governance")
def audit_governance():
    return GOVERNANCE

# Exemple: classification institutionnelle (journal)
class ClassificationIn(BaseModel):
    category: str
    language: Literal["fr", "es", "en", "sw", "ln"] = "fr"
    user: str = "jurist"

@app.post("/audit/classify")
def audit_classify(data: ClassificationIn):
    ev = log_classification(
        category=data.category,
        language=data.language,
        user=data.user,
        status="validated",
        notes="Décision juriste",
        governance_level="institutional"
    )
    return {"message": "Classification auditée", "event_id": ev.event_id}
