from peewee import ForeignKeyField

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

db.execute_sql('ALTER TABLE users DROP COLUMN IF EXISTS group_id CASCADE')
db.execute_sql('ALTER TABLE users DROP COLUMN IF EXISTS project_id CASCADE')
db.execute_sql('ALTER TABLE groups DROP COLUMN IF EXISTS teacher_id CASCADE')
db.execute_sql('''
        ALTER TABLE users 
        ADD COLUMN group_id INTEGER REFERENCES groups(id) ON DELETE SET NULL
    ''')

db.execute_sql('''
        ALTER TABLE users
        ADD COLUMN project_id INTEGER REFERENCES projects(id) ON DELETE SET NULL
    ''')

db.execute_sql('''
        ALTER TABLE groups
        ADD COLUMN teacher_id INTEGER REFERENCES users(id) ON DELETE SET NULL
    ''')

Users_orig = Users
Groups_orig = Groups


class Users(Users_orig):
    group = ForeignKeyField(Groups, column_name='group_id', backref='students', null=True)
    project = ForeignKeyField(Projects, column_name='project_id', backref='participants', null=True)


class Groups(Groups_orig):
    teacher = ForeignKeyField(Users, column_name='teacher_id', backref='teaches_groups', null=True)


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
