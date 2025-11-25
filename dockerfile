# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
ENV PORT=8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Backend
FROM python:3.11-slim AS backend
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app

# Frontend
FROM nginx:alpine AS frontend
COPY ui /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Final stage
FROM backend AS final
COPY --from=frontend /usr/share/nginx/html /usr/share/nginx/html
COPY --from=frontend /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
