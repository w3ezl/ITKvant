from peewee import CharField, IntegerField, DeferredForeignKey, BooleanField

from web_app import db
from web_app.models import BaseModel


class User(BaseModel):
    GENDER_CHOICES = ("male", "female")

    login = CharField(max_length=32, unique=True, null=False)
    password = CharField(null=False)
    group = DeferredForeignKey("Group", backref="students", column_name="group_id", null=True, field=IntegerField())
    is_teacher = BooleanField(default=False, null=False)
    rating_points = IntegerField(default=0)
    first_name = CharField(max_length=32)
    last_name = CharField(max_length=32)
    father_name = CharField(max_length=32)
    gender = CharField(choices=GENDER_CHOICES)
    status = CharField(null=True, max_length=150)
    project = DeferredForeignKey("Project", backref="participants", column_name="project_id", null=True, field=IntegerField())
