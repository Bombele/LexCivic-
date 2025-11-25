# Bitácora 3 — Déploiement UI + API

Ce jalon documente la mise en place du workflow de déploiement pour LexCivic.

---

## ⚙️ Architecture

- **Backend** : FastAPI (app/).
- **Frontend** : UI statique (ui/).
- **Proxy** : Nginx pour servir l’UI et rediriger `/api/` vers FastAPI.

---

## 🚀 Options de déploiement

- **Séparé** : API et UI déployées indépendamment (Render/Railway).
- **Combiné** : Docker multi‑service avec Nginx + Uvicorn.

---

## 📜 Narrativa institutionnelle

Ce déploiement garantit la **séparation claire des couches** et la **transparence citoyenne**.  
Il permet une **interopérabilité** et une **auditabilité** renforcées.

---

## 🧾 Commit associé

```bash
git add Dockerfile nginx.conf README.md bitacora/03-deployment.md
git commit -m "Bitácora 3: Workflow de déploiement UI + API avec Nginx et FastAPI"
