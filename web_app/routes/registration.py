from flask import request, flash, redirect, url_for, session, render_template
from peewee import IntegrityError
from werkzeug.security import generate_password_hash

from web_app import User, app
from web_app.routes._check_auth import is_login


@app.route("/registration", methods=["GET", "POST"])
def reg_page():
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")
        rep_password = request.form.get("rep_password")

        if password != rep_password:
            flash("Пароли не совпадают")
            return redirect(url_for("reg_page"))

        if User.select().where(User.login == login).exists():
            flash("Такой пользователь уже существует")
            return redirect(url_for("reg_page"))

        try:
            hashed_password = generate_password_hash(password)
            user = User.create(
                login=login,
                password=hashed_password,
                widget_token=generate_token(16)
            )
            session["login"] = user.login
            return redirect(url_for("dashboard_page"))
        except IntegrityError:
            flash("Ошибка: пользователь уже существует")
            return redirect(url_for("reg_page"))

    # GET-запрос
    if not is_login():
        return render_template("registration.html")
    return redirect(url_for("dashboard_page"))