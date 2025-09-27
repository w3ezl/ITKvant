from flask import request, url_for, render_template
from werkzeug.utils import redirect

from web_app import app, Groups, Users, RegistrationLinks
from web_app.routes._check_auth import is_login, current_user
from web_app.routes._generate_token import generate_token


@app.route("/reg_link/form", methods=["GET"])
def form_reg_link():
    if not is_login():
        return redirect(url_for("auth_page"))
    if not current_user().is_teacher:
        return 404
    groups = Groups.select()
    return render_template("reg_link_form.html", groups=groups)

@app.route("/reg_link", methods=["POST"])
def create_reg_link():
    if not is_login():
        return redirect(url_for("auth_page"))
    if not current_user().is_teacher:
        return 404
    count = int(request.form.get("count"))
    group_id = int(request.form.get("group"))
    for i in range(count):
        RegistrationLinks.create(
            code=generate_token(16),
            group=Groups.get(Groups.id == group_id)
        )
    return redirect(url_for("dashboard_page", page="admin", select="links"))
