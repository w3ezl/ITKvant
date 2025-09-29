from peewee import ForeignKeyField

from .base import BaseModel
from .task import Tasks
from .user import Users


class UserTasks(BaseModel):
    user = ForeignKeyField(Users, backref="tasks")
    task = ForeignKeyField(Tasks, backref="performers")
