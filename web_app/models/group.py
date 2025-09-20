from peewee import CharField, IntegerField, ForeignKeyField
from playhouse.postgres_ext import JSONField

from web_app import db
from web_app.models import BaseModel
from web_app.models.user import User

class Group(BaseModel):
    name = CharField(max_length=16, null=False)
    schedule = JSONField()
    teacher = ForeignKeyField(User, backref="teaches_groups", null=False)
    study_year = IntegerField(null=False)