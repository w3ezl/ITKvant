from peewee import CharField, IntegerField, ForeignKeyField, BooleanField

from web_app import db
from web_app.models import BaseModel
from web_app.models.group import Group


class User(BaseModel):
    login = CharField(max_length=32, unique=True, null=False)
    password = CharField(null=False)
    group = ForeignKeyField(Group, backref="students")
    is_teacher = BooleanField(default=False, null=False)
    rating_points = IntegerField(default=0)

