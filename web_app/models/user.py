from peewee import CharField, IntegerField, BooleanField, DeferredForeignKey
from web_app.models import BaseModel

class Users(BaseModel):
    GENDER_CHOICES = ("male", "female")

    login = CharField(max_length=32, unique=True, null=False)
    password = CharField(max_length=255, null=False)
    group = DeferredForeignKey('Groups', backref='students', column_name='group_id', null=True)
    is_teacher = BooleanField(default=False, null=False)
    rating_points = IntegerField(default=0, null=False)
    first_name = CharField(max_length=32, null=False)
    last_name = CharField(max_length=32, null=False)
    father_name = CharField(max_length=32, null=False)
    gender = CharField(choices=GENDER_CHOICES, null=False)
    status = CharField(max_length=150, null=True)
    project = DeferredForeignKey('Projects', backref='participants', column_name='project_id', null=True)
