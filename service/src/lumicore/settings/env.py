import os

from dotenv import load_dotenv

load_dotenv(override=True)

from lumicore.settings.base import *

SITE_ID = 1

DEBUG = os.getenv("DEBUG")

POSTGRES_DB = "lumicore_db"
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = "lumicore_db"

CORS_ALLOW_ALL_ORIGINS = bool(os.getenv("CORS_ALLOW_ALL_ORIGINS", False))

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = [
    "0.0.0.0",
    "localhost",
    "lumicore.dinho.dev"
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8003",
    "http://localhost:5173",
    "http://0.0.0.0:8003", 
    "https://lumicore.dinho.dev"
]

CORS_ALLOWED_ORIGINS = CSRF_TRUSTED_ORIGINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": POSTGRES_DB,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
        "HOST": DB_HOST,
        "PORT": 5432,
    }
}
