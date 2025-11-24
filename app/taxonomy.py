# app/taxonomy.py
taxonomy = {
    "COR-001": {
        "fr": "Corruption",
        "es": "Corrupción",
        "ln": "Kofinga mbongo"
    },
    "POW-002": {
        "fr": "Abus de pouvoir",
        "es": "Abuso de poder",
        "ln": "Kosalelaka makasi na botosi te"
    },
    "DIS-003": {
        "fr": "Discrimination judiciaire",
        "es": "Discriminación judicial",
        "ln": "Diskriminasyon ya bosambisi"
    },
    "DEL-004": {
        "fr": "Retards procéduraux",
        "es": "Demoras procesales",
        "ln": "Nkɔkɔ ya procédure"
    },
    "MED-005": {
        "fr": "Négligence médicale",
        "es": "Negligencia médica",
        "ln": "Koboya kosalela nsango ya santé"
    }
}

def get_taxonomy(lang="fr"):
    return {code: labels.get(lang, labels["fr"]) for code, labels in taxonomy.items()}
