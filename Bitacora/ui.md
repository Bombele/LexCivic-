# Bitácora 02 — Interface citoyenne multilingue (UI)

Ce jalon documente la création d’une **UI sobre et accessible**, multilingue (FR/ES/LN), connectée à l’API LexCivic.

---

## 🎯 Objectifs

- Traduire la taxonomie et la mémoire citoyenne en expérience simple.
- Garantir l’accessibilité mobile-first et la confiance visuelle.

---

## ⚙️ Composants

- Accueil avec mission et CTA.
- Formulaire de déclaration (type, lieu, date, description, upload).
- Sélecteur de langue visible.
- Timeline de mémoire (placeholder).
- Page Charte citoyenne.

---

## 🔌 Intégration API

- `/abuse-types` pour le select des catégories.
- `/reports` pour la création.
- `/stats` pour les filtres et la timeline.

---

## ♿ Accessibilité

Contraste élevé, navigation clavier, aria-live pour les statuts de formulaire.

---

## 🧾 Commit associé

```bash
git add index.html styles.css i18n.js app.js charte.html timeline.html README.md bitacora/02-ui.md
git commit -m "Bitácora 02: UI citoyenne multilingue (FR/ES/LN), mobile-first et accessible"
