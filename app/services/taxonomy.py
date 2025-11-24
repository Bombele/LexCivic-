import yaml
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "abuse_types.yaml"

def _load_taxonomy():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def get_abuse_labels(lang: str = "fr"):
    items = _load_taxonomy()
    return [f"{item['code']} – {item.get(lang, item.get('en', ''))}" for item in items]
