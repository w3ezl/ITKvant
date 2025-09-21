from peewee import ForeignKeyField

from web_app import db
from web_app.models import BaseModel
from web_app.models.task import Task
from web_app.models.user import User


class UserTask(BaseModel):
    user = ForeignKeyField(User, backref="tasks")
    task = ForeignKeyField(Task, backref="performers")
