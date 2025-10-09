from peewee import ForeignKeyField, CharField

from .base import BaseModel
from .user import Users


class UserQuests(BaseModel):
    user = ForeignKeyField(Users, backref="completed_quests")
    quest_name = CharField(32)

    class Meta:
        indexes = (
            (('user', 'quest_name'), True),
        )
