import os

from flask import request, url_for, render_template
from werkzeug.utils import redirect

from web_app import app, Group, User, Achievement
from web_app.routes._check_auth import is_login, current_user


@app.route("/achiv/<int:id>", methods=["DELETE"])
def delete_achiv(id):
    achiv = Achievement.get(Achievement.id == id)
    achiv.delete_instance()
    return ("", 204)

@app.route("/achiv/form", methods=["GET"])
def form_achiv():
    if not is_login():
        return redirect(url_for("auth_page"))
    if not current_user().is_teacher:
        return 404
    if request.args.get("id"):
        achiv = Achievement.get(Achievement.id == int(request.args.get("id")))
    else:
        achiv = {}
    return render_template("achiv_form.html", achiv=achiv)

@app.route("/achiv", methods=["POST"])
def create_achiv():
    if not is_login():
        return redirect(url_for("auth_page"))
    if not current_user().is_teacher:
        return 404

    title = request.form.get("title")
    desc = request.form.get("desc")
    file = request.files.get("icon")

    achiv = Achievement.create(title=title, description=desc)

    if file:
        filename = f"{achiv.id}.png"
        filepath = os.path.join(app.static_folder, "uploads", "achiv_icons", filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        file.save(filepath)

    return redirect(url_for("dashboard_page", page="admin", select="achivs"))
