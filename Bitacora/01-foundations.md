# Bitácora 1 — Fondations du projet JusticeDigitalMVP

Ce premier jalon documente la reprise du projet depuis zéro, en posant les bases techniques et institutionnelles.

---

## 🌍 Vision et Mission

- **Vision** : Construire une plateforme citoyenne multilingue pour documenter et classifier les abus institutionnels.
- **Mission** : Créer une mémoire institutionnelle transcontinentale, validée par la diaspora et conforme aux standards internationaux.
- **Objectif initial** : Déployer une ossature technique minimale avec endpoints clairs et taxonomie multilingue.

---

## 🧩 Architecture minimale

- **Backend** : FastAPI comme socle principal.
- **Endpoints initiaux** :
  - `/health` → vérifier l’état du système.
  - `/abuse-types` → exposer la taxonomie multilingue.
- **Taxonomie** : fichier `abuse_types.py` avec codes internes stables et traductions en 5 langues (fr, es, en, sw, ln).
- **Base de données** : SQLite pour démarrage rapide, extensible vers PostgreSQL.
- **CI/CD** : GitHub Actions pour validation automatique.

---

## 📜 Narrativa institutionnelle

Chaque étape technique est documentée comme un acte de mémoire et de résilience.  
Le Bitácora devient la trace vivante de la construction citoyenne et de la légitimité collective.

---

## 🚀 Prochaines étapes

- Bitácora 2 → Ajout de `/reports` pour enregistrer les dénonciations.
- Bitácora 3 → Endpoint `/stats` pour statistiques multilingues.
- Bitácora 4 → Intégration de spaCy pour NLP de base.
- Bitácora 5 → Déploiement initial sur Render avec CI/CD.

---

## 🧾 Commit associé

```bash
git add bitacora/01-foundations.md
git commit -m "Add Bitácora 1: Foundations of JusticeDigitalMVP"
