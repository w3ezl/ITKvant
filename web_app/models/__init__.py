from datetime import datetime, timezone
from peewee import Model, SQL, DateTimeField
from web_app import db

class BaseModel(Model):
    created_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    class Meta:
        database = db

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super().save(*args, **kwargs)

from web_app.models.user import Users
from web_app.models.achievement import Achievements
from web_app.models.group import Groups
from web_app.models.project import Projects
from web_app.models.registration_link import RegistrationLinks
from web_app.models.task import Tasks
from web_app.models.user_achievement import UserAchievements
from web_app.models.user_task import UserTasks

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
