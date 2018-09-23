import sys
import logging

from orator import Model
from orator import DatabaseManager

from decouple import config

DB_HOST = config("DB_HOST")
DB_NAME = config("DB_NAME")
DB_USER = config("DB_USER")
DB_PASS = config("DB_PASS")

jwt_settings = {"secret": config("JWT_SECRET"), "exp": 120, "algorithm": "HS256"}


DATABASES = {
    "postgres": {
        "driver": "postgres",
        "host": DB_HOST,
        "database": DB_NAME,
        "user": DB_USER,
        "password": DB_PASS,
        "prefix": "",
    }
}


db = DatabaseManager(DATABASES)
Model.set_connection_resolver(db)

# Logs

formatter = "%(asctime)s - %(module)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=formatter)
