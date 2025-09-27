from peewee import CharField, IntegerField, ForeignKeyField
from playhouse.postgres_ext import JSONField

from web_app.models import BaseModel


class Groups(BaseModel):
    name = CharField(max_length=16, null=False)
    schedule = JSONField()
    study_year = IntegerField(null=False)
    teacher = None
