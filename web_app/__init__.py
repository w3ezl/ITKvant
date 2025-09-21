import os
import pathlib
import logging

from flask import Flask
from peewee import PostgresqlDatabase

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), 'static')
)
app.secret_key = "208itkvant208rzhd"

VERSION_FILE = pathlib.Path(__file__).parent / ".version"
try:
    with open(VERSION_FILE) as f:
        app.config["APP_VERSION"] = f.read().strip()
except FileNotFoundError:
    app.config["APP_VERSION"] = "develop"

logging.basicConfig(filename='web_app/logs/main.log', level=logging.DEBUG)

db = PostgresqlDatabase(
    "it_kvant",
    user="postgres",
    password="kjkszpj",
    host="localhost",
    port=5432
)

from .models import *
from .routes import *
from .helpers import *

def init_db():
    if db.is_closed():
        db.connect()
