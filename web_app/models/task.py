from peewee import CharField, ForeignKeyField, IntegerField, DateTimeField

from web_app import db
from web_app.models import BaseModel
from web_app.models.project import Project
from web_app.models.user import User


class Task(BaseModel):
    title = CharField(64)
    project = ForeignKeyField(Project, backref="tasks")
    owner = ForeignKeyField(User, backref="owned_tasks")
    priority = IntegerField(default=0)
    deadline = DateTimeField()
