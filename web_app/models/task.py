from peewee import CharField, ForeignKeyField, IntegerField, DateTimeField

from .base import BaseModel
from web_app.models.project import Projects
from web_app.models.user import Users


class Tasks(BaseModel):
    title = CharField(64)
    project = ForeignKeyField(Projects, backref="tasks")
    owner = ForeignKeyField(Users, backref="owned_tasks")
    priority = IntegerField(default=0)
    deadline = DateTimeField()
