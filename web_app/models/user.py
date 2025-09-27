from peewee import CharField, IntegerField, BooleanField, ForeignKeyField
from web_app.models import BaseModel

class Users(BaseModel):
    GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))

    login = CharField(max_length=32, unique=True, null=False)
    password = CharField(null=False)
    first_name = CharField(max_length=32)
    last_name = CharField(max_length=32)
    father_name = CharField(max_length=32)
    gender = CharField(choices=GENDER_CHOICES)
    is_teacher = BooleanField(default=False)
    rating_points = IntegerField(default=0)
    status = CharField(null=True, max_length=150)
    group = ForeignKeyField(
        'Groups',
        backref='students',
        column_name='group_id',
        null=True
    )
