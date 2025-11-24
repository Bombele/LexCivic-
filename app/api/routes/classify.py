from fastapi import APIRouter, Query
from app.services.taxonomy import get_abuse_labels

router = APIRouter()

@router.get("", summary="Lister les types d’abus disponibles")
def list_labels(lang: str = Query("fr", description="Langue: fr, es, en, pt, ln")):
    return {"lang": lang, "labels": get_abuse_labels(lang)}
