from flask import session
from web_app.models.user import Users

def is_login():
    if "login" in session and Users.select().where(Users.login == session["login"]).exists():
        return True
    return False

def current_user():
    return Users.get(Users.login == session["login"])