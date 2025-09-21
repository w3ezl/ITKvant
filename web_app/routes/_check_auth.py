from flask import session
from web_app.models.user import User

def is_login():
    if "login" in session and User.select().where(User.login == session["login"]).exists():
        return True
    return False

def auth_user():
    return User.get(User.login == session["login"])