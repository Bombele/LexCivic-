# app/audit.py (optionnel)
import hashlib

def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
# app/audit.py
# Auditabilité automatique pour LexCivic: modèles, logger JSON, export, gouvernance.

from __future__ import annotations
from typing import Optional, Literal, Dict, Any
from datetime import datetime, date
import json
import uuid

from pydantic import BaseModel, Field, constr, validator

try:
    import yaml  # pyyaml recommandé (ajouter à requirements)
    HAS_YAML = True
except Exception:
    HAS_YAML = False

# --- Schéma Pydantic strict pour rapport citoyen ---

LangCode = Literal["fr", "es", "en", "sw", "ln"]
CategoryCode = constr(regex=r"^(COR-\d{3}|POW-\d{3}|DIS-\d{3}|DEL-\d{3}|MED-\d{3}|[a-z_]+)$")

class AbuseReport(BaseModel):
    category: CategoryCode = Field(..., description="Code interne stable ex: COR-001")
    description: constr(min_length=10) = Field(..., description="Description détaillée")
    date: date = Field(..., description="Date de l'événement")
    country: constr(min_length=2, max_length=64) = Field(..., description="Pays (libellé)")
    language: LangCode = Field(..., description="Langue de saisie")
    place: Optional[constr(max_length=128)] = Field(None, description="Lieu précisé")
    source: Optional[constr(max_length=64)] = Field("web", description="web, mobile, partner")
    user: Optional[constr(max_length=64)] = Field("anonymous", description="Identifiant, sinon anonyme")

    @validator("date")
    def not_future(cls, v):
        if v > date.today():
            raise ValueError("La date ne peut pas être future")
        return v

# --- Schéma d’événement d’audit standardisé ---

ActionType = Literal["declaration", "classification", "modification", "validation", "export"]
StatusType = Literal["received", "validated", "rejected", "error", "published"]

class AuditEvent(BaseModel):
    event_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    action: ActionType
    status: StatusType
    language: LangCode
    user: str = "anonymous"
    category: Optional[str] = None
    payload: Optional[Dict[str, Any]] = None
    notes: Optional[str] = None
    governance_level: Optional[Literal["automatic", "collaborative", "institutional"]] = "automatic"

# --- Logger JSON mémoire (peut être remplacé par stockage DB/S3) ---

class AuditLogger:
    def __init__(self):
        self._events: list[AuditEvent] = []

    def log(self, event: AuditEvent) -> AuditEvent:
        self._events.append(event)
        return event

    def all(self) -> list[Dict[str, Any]]:
        return [json.loads(e.json()) for e in self._events]

    def by_action(self, action: ActionType) -> list[Dict[str, Any]]:
        return [json.loads(e.json()) for e in self._events if e.action == action]

    def export_json(self) -> str:
        return json.dumps(self.all(), ensure_ascii=False, indent=2)

    def export_yaml(self) -> str:
        if not HAS_YAML:
            raise RuntimeError("PyYAML non disponible. Ajoute 'PyYAML' à requirements.txt.")
        return yaml.safe_dump(self.all(), sort_keys=False, allow_unicode=True)

# --- Schémas de gouvernance simples ---

GOVERNANCE: Dict[str, Any] = {
    "levels": {
        "automatic": {
            "description": "Validation syntaxique et taxonomique (Pydantic + règles)",
            "validators": ["pydantic_schema", "taxonomy_codes", "date_not_future"]
        },
        "collaborative": {
            "description": "Validation citoyenne (votes, consensus, feedback)",
            "mechanisms": ["votes>=3", "consensus>=0.6"]
        },
        "institutional": {
            "description": "Validation par juristes/ONG partenaires",
            "roles": ["jurist", "ngo_validator"],
            "records": ["decision_note", "review_timestamp"]
        },
    },
    "export": {
        "formats": ["json", "yaml"],
        "scope": ["application", "institutional", "citizen"]
    }
}

# Instance globale (peut être injectée)
audit_logger = AuditLogger()

# --- Helpers d’intégration ---

def log_declaration(report: AbuseReport, status: StatusType = "received", notes: Optional[str] = None):
    ev = AuditEvent(
        action="declaration",
        status=status,
        language=report.language,
        user=report.user or "anonymous",
        category=report.category,
        payload=report.dict(),
        notes=notes,
        governance_level="automatic",
    )
    return audit_logger.log(ev)

def log_classification(category: str, language: LangCode, user: str = "anonymous", status: StatusType = "validated", notes: Optional[str] = None, governance_level: str = "institutional"):
    ev = AuditEvent(
        action="classification",
        status=status,
        language=language,
        user=user,
        category=category,
        payload=None,
        notes=notes,
        governance_level=governance_level,  # "collaborative" ou "institutional"
    )
    return audit_logger.log(ev)

def log_export(format_: Literal["json", "yaml"], user: str = "anonymous", notes: Optional[str] = None):
    ev = AuditEvent(
        action="export",
        status="published",
        language="fr",
        user=user,
        category=None,
        payload={"format": format_},
        notes=notes,
        governance_level="automatic",
    )
    return audit_logger.log(ev)
