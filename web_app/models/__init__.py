from datetime import datetime, timezone
from peewee import Model, SQL, DateTimeField, ForeignKeyField
from web_app import db

class BaseModel(Model):
    created_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    class Meta:
        database = db

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super().save(*args, **kwargs)

from .group import Groups
from .user import Users
from .project import Projects
from .achievement import Achievements
from .task import Tasks
from .user_achievement import UserAchievements
from .user_task import UserTasks
from .registration_link import RegistrationLinks

tables = [Groups, Users, Projects, Achievements, RegistrationLinks, Tasks, UserAchievements, UserTasks]
db.create_tables(tables, safe=True)

__all__ = [
    "BaseModel",
    "Users",
    "Achievements",
    "Groups",
    "Projects",
    "RegistrationLinks",
    "Tasks",
    "UserAchievements",
    "UserTasks"
]
