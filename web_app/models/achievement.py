from peewee import CharField

from .base import BaseModel


class Achievements(BaseModel):
    title = CharField(32)
    description = CharField(128)
