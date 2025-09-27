from flask import render_template, redirect, url_for

from web_app import app, User, Group, RegistrationLink, Achievement
from web_app.routes._check_auth import is_login, current_user

@app.route("/admin_groups", methods=["GET"])
def admin_groups():
    if not is_login():
        return redirect(url_for("auth_page"))
    if not current_user().is_teacher:
        return 403
    groups = Group.select()
    return render_template("dashboard/admin_groups.html", groups=groups)


@app.route("/admin_links", methods=["GET"])
def admin_links():
    if not is_login():
        return redirect(url_for("auth_page"))
    if not current_user().is_teacher:
        return 403
    reg_links = RegistrationLink.select()
    return render_template("dashboard/admin_reg_links.html", reg_links=reg_links)


@app.route("/admin_profiles", methods=["GET"])
def admin_profiles():
    if not is_login():
        return redirect(url_for("auth_page"))
    if not current_user().is_teacher:
        return 403
    users = User.select()
    return render_template("dashboard/admin_profiles.html", users=users)


@app.route("/admin_achivs", methods=["GET"])
def admin_achivs():
    if not is_login():
        return redirect(url_for("auth_page"))
    if not current_user().is_teacher:
        return 403
    achivs = Achievement.select()
    return render_template("dashboard/admin_achivs.html", achivs=achivs)