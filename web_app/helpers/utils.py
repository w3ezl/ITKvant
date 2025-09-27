import os

from flask import url_for, session

from web_app import app, Users
from web_app.routes._check_auth import is_login


@app.context_processor
def utility_processor():
    if is_login():
        current_user = Users.get(Users.login == session["login"])
    else:
        current_user = {}
    def static_versioned(filename):
        if filename.split("/")[:2] == ["uploads", "avatars"]:
            avatar_id = filename.split("/")[-1].split(".")[0]
            file_path = os.path.join(app.static_folder, "uploads", "avatars", f"{avatar_id}.png")
            if not os.path.exists(file_path):
                filename = "img/unknown_user.svg"
        return url_for("static", filename=filename) + "?v=" + app.config["APP_VERSION"]
    def version_view():
        return app.config["APP_VERSION"]
    return dict(
        static_versioned=static_versioned,
        version_view=version_view,
        current_user=current_user
    )