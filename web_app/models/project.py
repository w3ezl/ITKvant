from peewee import CharField, ForeignKeyField

from .base import BaseModel
from web_app.models.user import Users


class Projects(BaseModel):
    title = CharField(32, null=False)
    description = CharField(32, null=False)
    manager = ForeignKeyField(Users, backref="managed_project", null=True)
