from peewee import CharField, IntegerField
from playhouse.postgres_ext import JSONField
from .base import BaseModel


class Groups(BaseModel):
    name = CharField(max_length=16, null=False)
    schedule = JSONField(null=True)
    study_year = IntegerField(null=False)

