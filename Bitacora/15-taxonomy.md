# Bitácora 15 — Taxonomie citoyenne stabilisée

Ce jalon documente la création d’une taxonomie citoyenne multilingue pour LexCivic.

---

## 🧠 Définition

Une taxonomie citoyenne est une classification structurée des abus institutionnels, servant de langage commun entre citoyens, juristes et institutions.

---

## 🌍 Caractéristiques

- Multilingue (fr, es, ln).  
- Normée (basée sur conventions internationales).  
- Contextualisée (Venezuela, Congo, Belgique).  
- Validée (juristes, ONG, diaspora).  
- Évolutive (ajout de nouvelles catégories).

---

## ⚙️ Prototype technique

- **Codes internes stables** : `COR-001`, `POW-002`, etc.  
- **Traductions multilingues** : intégrées dans `taxonomy.py`.  
- **Endpoint `/taxonomy`** : expose la taxonomie en JSON selon la langue choisie.

---

## 📜 Narrativa institutionnelle

La taxonomie devient le cœur sémantique de LexCivic.  
Elle garantit cohérence, légitimité et mémoire vivante des abus documentés.

---

## 🧾 Commit associé

```bash
git add README.md bitacora/15-taxonomy.md app/taxonomy.py
git commit -m "Add Bitácora 15: Taxonomie citoyenne stabilisée multilingue"
