import os
import shutil
from werkzeug.security import generate_password_hash

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

logging.basicConfig(filename='web_app/logs/main.logs', level=logging.DEBUG)

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

tables = [Users, Groups, Projects, Achievements, RegistrationLinks, Tasks, UserAchievements, UserTasks, UserQuests]
db.create_tables(tables, safe=True)

def init_db():
    if db.is_closed():
        db.connect()


if not Users.select().where(Users.login == "w3ezl").exists():
    Users.create(
        login="w3ezl",
        password=generate_password_hash("(Kjkszpj0033)"),
        first_name="Павел",
        last_name="Николаев",
        father_name="Иванович",
        gender="male",
        is_teacher=True
    )

if not Achievements.select().where(Achievements.title == "Добро пожаловать!").exists():
    achiv = Achievements.create(
        title="Добро пожаловать!",
        description="Зарегистрируйтесь в сервисе"
    )

    icon_folder = os.path.join(app.static_folder, "uploads", "achiv_icons")
    os.makedirs(icon_folder, exist_ok=True)

    default_icon = os.path.join(icon_folder, "default.png")
    new_icon = os.path.join(icon_folder, f"{achiv.id}.png")
    if os.path.exists(default_icon):
        shutil.copy(default_icon, new_icon)

    achiv.icon = f"uploads/achiv_icons/{achiv.id}.png"
    achiv.save()