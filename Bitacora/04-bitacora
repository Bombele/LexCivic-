# Bitácora 4 — Auditabilité automatique

Ce jalon formalise l’auditabilité intégrée de LexCivic: validation Pydantic, journalisation JSON, export et gouvernance.

---

## 🎯 Objectifs

- Traçabilité complète des actions citoyennes et institutionnelles.
- Conformité sémantique et technique (schémas stricts).
- Transparence auditable (exports JSON/YAML).

---

## ⚙️ Implémentation

- `app/audit.py` — module modulaire d’audit:
  - `AbuseReport` (Pydantic) — validation stricte des déclarations.
  - `AuditEvent` — format standardisé des événements.
  - `AuditLogger` — logger JSON en mémoire + export YAML/JSON.
  - `GOVERNANCE` — niveaux de validation (automatic/collaborative/institutional).
  - Helpers: `log_declaration`, `log_classification`, `log_export`.

- Intégration API:
  - `POST /reports/audited` — création + journalisation.
  - `GET /audit/logs` — export JSON/YAML.
  - `GET /audit/governance` — schéma de gouvernance.
  - `POST /audit/classify` — décisions institutionnelles.

---

## ♿ Sécurité et prudence

- Anonymisation par défaut (`user: "anonymous"`).
- Contrôle de la date (pas de futur).
- Codes taxonomiques stables en entrée.

---

## 🧾 Commit associé

```bash
git add app/audit.py app/main.py README.md bitacora/04-audit.md requirements.txt
git commit -m "Bitácora 4: Auditabilité automatique (Pydantic + logger JSON + export YAML/JSON + gouvernance)"
