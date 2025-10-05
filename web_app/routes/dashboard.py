from web_app import app, Users
from web_app.routes._check_auth import is_login, current_user

from flask import redirect, url_for, render_template


@app.route("/dashboard", methods=["GET"])
def dashboard_page():
    if not is_login():
        return redirect(url_for("auth_page"))
    return render_template("dashboard.html")

@app.route("/rating_table", methods=["GET"])
def rating_table():
    if not is_login():
        return redirect(url_for("auth_page"))
    students = (
        Users
        .select()
        .where(Users.is_teacher == False)
        .order_by(Users.rating_points.desc(), Users.created_at.asc())
    )
    return render_template("dashboard/rating_table.html", students=students)

@app.route("/admin", methods=["GET"])
def admin():
    if not is_login():
        return redirect(url_for("auth_page"))
    if not current_user().is_teacher:
        return 403
    return render_template("dashboard/admin.html")