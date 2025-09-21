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

from web_app.models.user import User
from web_app.models.achievement import Achievement
from web_app.models.group import Group
from web_app.models.project import Project
from web_app.models.registration_link import RegistrationLink
from web_app.models.task import Task
from web_app.models.user_achievement import UserAchievement
from web_app.models.user_task import UserTask

__all__ = [
    "BaseModel",
    "User",
    "Achievement",
    "Group",
    "Project",
    "RegistrationLink",
    "Task",
    "UserAchievement",
    "UserTask"
]
