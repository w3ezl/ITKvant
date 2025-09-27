from peewee import CharField

from web_app import db
from web_app.models import BaseModel


class Achievements(BaseModel):
    title = CharField(32)
    description = CharField(128)
