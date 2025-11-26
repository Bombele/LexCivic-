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
# LexCivic — Interface citoyenne multilingue

LexCivic traduit la justice digitale en une **expérience citoyenne sobre, mobile-first et auditable**.  
UI construite en **HTML/CSS/JS** et intégrée à l’API **FastAPI**.

---

## 🎯 Objectifs UI

- Accessibilité universelle, confiance visuelle, multilinguisme fluide (FR/ES/LN).
- Déclaration simple d’abus, mémoire institutionnelle, charte citoyenne.

---

## 📦 Structure

- `index.html` — Accueil + formulaire de déclaration.
- `charte.html` — Charte citoyenne et gouvernance.
- `timeline.html` — Mémoire institutionnelle (timeline).
- `styles.css` — Design minimaliste et accessible.
- `i18n.js` — Dictionnaire de traductions FR/ES/LN.
- `app.js` — Logique UI et intégration API.

---

## 🔌 Intégration API

- `/abuse-types` pour alimenter les sélecteurs.
- `/reports` pour enregistrer les dénonciations.
- `/stats` pour alimenter la mémoire et les filtres.

Configurer `API.base` dans `app.js` (ex: `https://api.lexcivic.org`).

---

## 🚀 Démarrage

Servir les fichiers statiques (ex: `python -m http.server`) ou via un hébergeur statique.  
Connecter à l’API FastAPI déployée (Render/Railway).

---

## ♿ Accessibilité

Contraste élevé, navigation clavier, aria-labels, focus visible, mobile-first.

---

## ⚖️ Disclaimer

L’UI est informative et citoyenne.  
Elle ne remplace pas l’assistance juridique professionnelle.
## 🚀 Déploiement

LexCivic est déployé en deux couches :

- **Backend (FastAPI)** → endpoints `/reports`, `/stats`, `/consultation`, etc.
- **Frontend (UI statique)** → pages HTML/CSS/JS (`ui/`).

### Option 1 : Déploiement séparé
- Backend sur Render/Railway (service API).
- Frontend sur Render/Railway (site statique).

### Option 2 : Déploiement combiné
- Docker multi‑service avec Nginx servant l’UI et proxy vers FastAPI.

### CI/CD
- GitHub Actions pour build/test.
- Déploiement automatique sur push.
## 🔍 Auditabilité automatique

LexCivic implémente une **auditabilité intégrée** :
- Modèles Pydantic stricts pour valider les données citoyennes.
- Logger JSON standardisé pour chaque action (déclaration, classification, export).
- Export des logs en **JSON** et **YAML** pour audit externe.
- Schéma de gouvernance simple (automatic, collaborative, institutional).

### Endpoints d’audit
- `POST /reports/audited` — crée une déclaration et journalise l’événement (Pydantic + audit).
- `GET /audit/logs?format=json|yaml` — exporte les logs pour audit externe.
- `GET /audit/governance` — expose le schéma de gouvernance.
- `POST /audit/classify` — journalise une décision de classification (juriste/ONG).

Ces mécanismes renforcent la **confiance**, la **transparence** et l’**audibilité**.
# ITCAA – Interface citoyenne et certification DIH

## 🌍 Présentation
ITCAA (Institut Transnational de Certification et d’Architecture d’Appui) est une initiative citoyenne et institutionnelle fondée par **Camille Bombele Liyama** (homme, fondateur et développeur principal).  
Le projet vise à offrir une **justice digitale**, une **certification en droit international humanitaire (DIH)** et une **mémoire institutionnelle** pour la diaspora et les partenaires internationaux.

---

## 🚀 Objectifs
- **Certification DIH** : offrir une base technique et institutionnelle pour la reconnaissance des acteurs.
- **Mémoire citoyenne** : documenter chaque jalon technique comme acte de résilience et d’empowerment.
- **Multilinguisme stratégique** : interface et rapports disponibles en plusieurs langues.
- **Cartographie interactive** : visualiser les acteurs, partenaires et risques institutionnels.
- **Auditabilité** : garantir la transparence et la légitimité des systèmes.

---

## 🧑‍💻 Développeur principal
- **Camille Bombele Liyama**  
  - Fondateur et architecte institutionnel  
  - Développeur principal (FastAPI, SQLAlchemy, CI/CD, multilinguisme, i18n)  
  - Porteur du projet **LexCivic** et responsable de la légitimation institutionnelle  

---

## ⚙️ Stack technique
- **Backend** : FastAPI + Uvicorn
- **Base de données** : PostgreSQL (Render Cloud)
- **ORM** : SQLAlchemy
- **Validation** : Pydantic
- **Multilinguisme** : i18n avec YAML
- **Cartographie** : Leaflet JS
- **CI/CD** : GitHub Actions + Render
- **Tests** : Pytest + HTTPX

---

## 📦 Installation locale

```bash
git clone https://github.com/ton-org/ITCAA.git
cd ITCAA
pip install -r requirements.txt
export DATABASE_URL="postgresql://user:password@localhost:5432/itcaa"
PYTHONPATH=src python -m uvicorn apps.api.main:app --reload
