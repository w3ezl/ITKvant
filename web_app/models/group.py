from peewee import CharField, IntegerField, ForeignKeyField
from playhouse.postgres_ext import JSONField
from web_app.models import BaseModel  # подкорректируй импорт, если у тебя иначе

class Groups(BaseModel):
    name = CharField(max_length=16, null=False)
    schedule = JSONField(null=True)
    study_year = IntegerField(null=False)

    # Связь с учителем (пользователем)
    teacher = ForeignKeyField(
        'Users',
        backref='teaches_groups',
        column_name='teacher_id',
        null=True
    )
