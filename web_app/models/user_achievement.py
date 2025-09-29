from peewee import ForeignKeyField

from .base import BaseModel
from .achievement import Achievements
from .user import Users


class UserAchievements(BaseModel):
    user = ForeignKeyField(Users, backref="achievements")
    achievement = ForeignKeyField(Achievements, backref="owners")
