from peewee import ForeignKeyField

from web_app import db
from web_app.models import BaseModel
from web_app.models.achievement import Achievement
from web_app.models.user import User


class UserAchievement(BaseModel):
    user = ForeignKeyField(User, backref="achievements")
    achievement = ForeignKeyField(Achievement, backref="owners")
