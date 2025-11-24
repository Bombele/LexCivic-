# LexCivic-
LexCivic est une API citoyenne multilingue basée sur FastAPI. Elle expose une taxonomie d’abus institutionnels en plusieurs langues et fournit des endpoints pour classification et documentation. Ossature légère, évolutive et déployée sur Render, elle servira de socle à l’intégration NLP et fiches PEC.
# JusticeDigitalMVP / LexCivic

Plataforma ciudadana multilingüe para documentar abusos institucionales y fortalecer la justicia digital transcontinental.  
Construida con **FastAPI, SQLAlchemy, spaCy, Hugging Face Transformers**.

---

## 🌍 Vision

- **Mission** : Créer une mémoire institutionnelle transcontinentale validée par la diaspora.  
- **Objectif** : Documenter, classifier et auditer abus institutionnels en 5 langues (fr, es, en, sw, ln).  
- **Valeurs** : Transparence, légitimité collective, empowerment citoyen.

---

## 🧩 Endpoints disponibles (Phase 1)

- **`/health`** → Vérification du système.  
- **`/abuse-types`** → Taxonomie multilingue des abus institutionnels.  
- **`/reports`** → Dépôt de dénonciations citoyennes.  
- **`/stats`** → Statistiques multilingues des abus.  
- **`/consultation`** → IA conversationnelle juridique (informative, non substitutive à un avocat).

---

## 🌍 Taxonomie multilingue

Chaque abus est identifié par un **code interne stable** et traduit en 5 langues.  
Exemple :  
- `abuse_of_power` → "Abus de pouvoir" (fr), "Abuso de poder" (es), "Abuse of power" (en), "Matumizi mabaya ya mamlaka" (sw), "Kosalelaka makasi na botosi te" (ln).

---

## 🧠 IA Conversacional

- **spaCy** → NLP de base.  
- **Hugging Face Transformers (xlm-roberta-base)** → Classification multilingue robuste.  
- **Endpoint `/consultation`** → Détection automatique des abus dans les questions citoyennes.  

Ejemplo:

```http
POST /consultation?lang=es
{
  "user": "Camille",
  "question": "El funcionario me pidió dinero para procesar mi caso"
}
# JusticeDigitalMVP / LexCivic

Plataforma ciudadana multilingüe para documentar abusos institucionales y fortalecer la justicia digital transcontinental.  
Construida con **FastAPI, SQLAlchemy, spaCy, Hugging Face Transformers**.

---

## 🌍 Vision

- **Mission** : Créer une mémoire institutionnelle transcontinentale validée par la diaspora.  
- **Objectif** : Documenter, classifier et auditer abus institutionnels en 5 langues (fr, es, en, sw, ln).  
- **Valeurs** : Transparence, légitimité collective, empowerment citoyen.

---

## 🧩 Endpoints disponibles

- **`/health`** → Vérification du système.  
- **`/abuse-types`** → Taxonomie multilingue des abus institutionnels.  
- **`/taxonomy`** → Taxonomie citoyenne stabilisée avec codes internes.  
- **`/reports`** → Dépôt de dénonciations citoyennes.  
- **`/stats`** → Statistiques multilingues des abus.  
- **`/consultation`** → IA conversationnelle juridique (informative, non substitutive à un avocat).

---

## 🌍 Taxonomie citoyenne stabilisée

Chaque abus est identifié par un **code interne stable** et traduit en plusieurs langues.  
Exemple :  
- `COR-001` → "Corruption" (fr), "Corrupción" (es), "Kofinga mbongo" (ln).  
- `POW-002` → "Abus de pouvoir" (fr), "Abuso de poder" (es), "Kosalelaka makasi na botosi te" (ln).

---

## 📜 Bitácora

La mémoire active du projet est documentée dans la carpeta `bitacora/`.  
- **01-foundations.md** → Fondations du projet.  
- **02-reports.md** → Endpoint `/reports`.  
- **03-stats.md** → Endpoint `/stats`.  
- **13-ai-integration.md** → IA conversacional jurídica.  
- **14-dcat.md** → Interoperabilidad con DCAT.  
- **15-taxonomy.md** → Taxonomie citoyenne stabilisée.

---

## ⚖️ Disclaimer

Cette plateforme est informative et citoyenne.  
Elle ne remplace pas l’assistance juridique professionnelle.
