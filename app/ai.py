# app/ai.py
from transformers import pipeline

# Remplace par ton modèle fine-tuné si disponible
CLASSIFIER_MODEL = "xlm-roberta-base"
classifier = pipeline("text-classification", model=CLASSIFIER_MODEL, tokenizer=CLASSIFIER_MODEL)

def classify_question(text: str):
    # Retourne (label, score) ou (None, 0.0)
    try:
        res = classifier(text, truncation=True)[0]
        return res.get("label"), float(res.get("score", 0))
    except Exception:
        return None, 0.0
