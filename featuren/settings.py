import os
import sys
import logging

from orator import Model
from orator import DatabaseManager
from py_database_url import orator

DATABASES = orator()

db = DatabaseManager(DATABASES)
Model.set_connection_resolver(db)

jwt_settings = {
    "secret": os.environ.get("JWT_SECRET"),
    "exp": 120,
    "algorithm": "HS256",
}

# Logs

formatter = "%(asctime)s - %(module)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=formatter)
