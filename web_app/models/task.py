from peewee import CharField, ForeignKeyField, IntegerField, DateTimeField

from .base import BaseModel
from .project import Projects
from .user import Users


class Tasks(BaseModel):
    title = CharField(64)
    project = ForeignKeyField(Projects, backref="tasks")
    owner = ForeignKeyField(Users, backref="owned_tasks")
    priority = IntegerField(default=0)
    deadline = DateTimeField()
