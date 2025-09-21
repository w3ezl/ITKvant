from peewee import CharField, ForeignKeyField

from web_app import db
from web_app.models import BaseModel
from web_app.models.user import User


class Project(BaseModel):
    title = CharField(32, null=False)
    description = CharField(32, null=False)
    manager = ForeignKeyField(User, backref="managed_project", null=True)
