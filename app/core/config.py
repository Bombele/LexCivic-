import os

class Settings:
    APP_NAME: str = "LexCivic"
    ENV: str = os.getenv("ENV", "production")
    # Ajoute ici les clés (DB_URL, secrets, etc.)

settings = Settings()
