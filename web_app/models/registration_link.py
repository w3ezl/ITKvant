from peewee import CharField, ForeignKeyField

from web_app import db
from web_app.models import BaseModel
from web_app.models.group import Group


class RegistrationLink(BaseModel):
    group = ForeignKeyField(Group, backref="reg_links")
    code = CharField(16, unique=True)
