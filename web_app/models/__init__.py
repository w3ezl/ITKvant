from web_app import db

from .base import BaseModel
from .user import Users
from .group import Groups
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
