from peewee import CharField, IntegerField, ForeignKeyField
from playhouse.postgres_ext import JSONField

from .base import BaseModel  # Предположим, что BaseModel импортирует db


class Groups(BaseModel):
    name = CharField(max_length=16, null=False)
    schedule = JSONField()  # Расписание (JSON)
    study_year = IntegerField(null=False)

    teacher = ForeignKeyField(
        'Users',
        backref='teaches_groups',
        column_name='teacher_id',
        null=True
    )
