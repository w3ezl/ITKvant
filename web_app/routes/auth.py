from werkzeug.security import check_password_hash

from web_app import app, User
from web_app.routes._check_auth import is_login

from flask import redirect, url_for, render_template, request, session, flash


@app.route("/auth", methods=["GET", "POST"])
def auth_page():
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")

        try:
            user = User.get(User.login == login)
        except User.DoesNotExist:
            flash("Неверный логин или пароль")
            return redirect(url_for("auth_page"))

        if user and check_password_hash(user.password, password):
            session["login"] = user.login
            return redirect(url_for("dashboard_page"))
        else:
            flash("Неверный логин или пароль")
            return redirect(url_for("auth_page"))

    if not is_login():
        return render_template("auth.html")
    return redirect(url_for("dashboard_page"))

@app.route("/logout", methods=["GET"])
def logout():
    if is_login():
        session.clear()
    return redirect(url_for("auth_page"))