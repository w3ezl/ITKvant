from peewee import ForeignKeyField

from web_app import db
from web_app.models import BaseModel
from web_app.models.achievement import Achievements
from web_app.models.user import Users


class UserAchievements(BaseModel):
    user = ForeignKeyField(Users, backref="achievements")
    achievement = ForeignKeyField(Achievements, backref="owners")
