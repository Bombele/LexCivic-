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
