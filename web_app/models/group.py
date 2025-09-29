from peewee import CharField, IntegerField, ForeignKeyField
from playhouse.postgres_ext import JSONField
from .base import BaseModel
from .user import Users


class Groups(BaseModel):
    name = CharField(max_length=16, null=False)
    schedule = JSONField(null=True)
    study_year = IntegerField(null=False)
    teacher = ForeignKeyField(Users, backref="teaches_groups", null=True)

