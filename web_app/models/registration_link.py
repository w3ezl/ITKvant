from peewee import CharField, ForeignKeyField

from web_app.models import BaseModel
from web_app.models.group import Group


class RegistrationLink(BaseModel):
    group = ForeignKeyField(Group, backref="reg_links")
    code = CharField(16, unique=True)

    @property
    def url(self):
        return f"https://itkvantum.ru/registration?code={self.code}"
