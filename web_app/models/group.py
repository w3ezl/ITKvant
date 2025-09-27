from peewee import CharField, IntegerField, DeferredForeignKey
from playhouse.postgres_ext import JSONField
from .base import BaseModel

class Groups(BaseModel):
    name = CharField(max_length=16, null=False)
    schedule = JSONField(null=True)
    study_year = IntegerField(null=False)

    teacher = DeferredForeignKey(
        'Users',
        backref='teaches_groups',
        column_name='teacher_id',
        null=True
    )
