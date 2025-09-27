from peewee import CharField, IntegerField, BooleanField, ForeignKeyField

from .base import BaseModel


class Users(BaseModel):
    GENDER_CHOICES = (("male", "Мужской"), ("female", "Женский"))

    login = CharField(max_length=32, unique=True, null=False)
    password = CharField(null=False)

    group = ForeignKeyField(
        'Groups',
        backref='students',
        column_name='group_id',
        null=True
    )

    is_teacher = BooleanField(default=False)
    rating_points = IntegerField(default=0)

    first_name = CharField(max_length=32)
    last_name = CharField(max_length=32)
    father_name = CharField(max_length=32)
    gender = CharField(choices=GENDER_CHOICES)
    status = CharField(null=True, max_length=150)

    project = ForeignKeyField(
        'Projects',
        backref='participants',
        column_name='project_id',
        null=True
    )
