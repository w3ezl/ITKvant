import os
import shutil

from flask import request, flash, redirect, url_for, session, render_template
from peewee import IntegrityError
from werkzeug.security import generate_password_hash

from web_app import User, app, RegistrationLink, Group, Achievement, UserAchievement
from web_app.routes._check_auth import is_login


@app.route("/registration", methods=["GET", "POST"])
def reg_page():
    code = request.args.get("code")
    if request.method == "POST":
        reg_link = RegistrationLink.get(RegistrationLink.code == code)
        login = request.form.get("login")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        father_name = request.form.get("father_name")
        gender = request.form.get("gender")
        group = RegistrationLink.get(RegistrationLink.code == code).group

        if password != password2:
            flash("Пароли не совпадают")
            return redirect(url_for("reg_page"))

        if User.select().where(User.login == login).exists():
            flash("Пользователь с таким логином уже существует")
            return redirect(url_for("reg_page"))

        try:
            hashed_password = generate_password_hash(password)
            user = User.create(
                login=login,
                password=hashed_password,
                first_name=first_name,
                last_name=last_name,
                father_name=father_name,
                gender=gender,
                group=group
            )
            old_avatar_path = os.path.join(app.static_folder, "uploads", "avatars", f"{reg_link.code}.png")
            new_avatar_path = os.path.join(app.static_folder, "uploads", "avatars", f"{user.id}.png")

            if os.path.exists(old_avatar_path):
                shutil.move(old_avatar_path, new_avatar_path)
            reg_link.delete_instance()
            default_achiv = Achievement.get(Achievement.title == "Добро пожаловать!")
            if default_achiv:
                UserAchievement.create(user=user, achievement=default_achiv)
            session["login"] = user.login
            return redirect(url_for("dashboard_page"))
        except IntegrityError:
            flash("Ошибка: пользователь уже существует")
            return redirect(url_for("reg_page"))

    # GET-запрос
    if not is_login():
        try:
            group = RegistrationLink.get(RegistrationLink.code == code).group
            teacher = group.teacher
            return render_template("registration.html", group=group, teacher=teacher)
        except:
            flash("Данная ссылка недействительна")
            return render_template("registration_error.html")
    return redirect(url_for("dashboard_page"))