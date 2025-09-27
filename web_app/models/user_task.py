from peewee import ForeignKeyField

from .base import BaseModel
from web_app.models.task import Tasks
from web_app.models.user import Users


class UserTasks(BaseModel):
    user = ForeignKeyField(Users, backref="tasks")
    task = ForeignKeyField(Tasks, backref="performers")
