from flask import render_template, redirect, url_for, flash, request, abort

from web_app import app, Achievements, UserAchievements
from web_app.routes._check_auth import is_login, current_user


@app.route("/october_2025", methods=["GET"])
def page_quest_10_2025():
    if not is_login():
        return redirect(url_for("auth_page"))
    achiv = Achievements.get(Achievements.title == "Криптограф Цезаря")
    if UserAchievements.select().where(UserAchievements.achievement == achiv):
        abort(404)
    return render_template("quest_october_2025.html", word_1="", word_2="", word_3="")


@app.route("/october_2025", methods=["POST"])
def post_quest_10_2025():
    if not is_login():
        return redirect(url_for("auth_page"))
    achiv = Achievements.get(Achievements.title == "Криптограф Цезаря")
    if UserAchievements.select().where(UserAchievements.achievement == achiv):
        abort(404)
    word_1 = request.form.get("word_1")
    word_2 = request.form.get("word_2")
    word_3 = request.form.get("word_3")
    if word_1.lower() == "кванториум" and word_2.lower() == "маяковский" and word_3.lower() == "цезарь":
        user = current_user()
        if achiv:
            UserAchievements.create(user=user, achievement=achiv)
        user.rating_points = 999999
        user.save()
        return redirect(url_for("dashboard_page"))
    else:
        if word_1.lower() == "первое слово" or word_2.lower() == "второе слово" or word_3.lower() == "третье слово":
            flash("Вряд ли было бы так просто)")
            word_1 = word_2 = word_3 = ""
        else:
            flash_str = ""
            if word_1.lower() != "кванториум":
                flash_str += "1 неверно, "
                word_1 = ""
            if word_2.lower() != "маяковский":
                flash_str += "2 неверно, "
                word_2 = ""
            if word_3.lower() != "цезарь":
                flash_str += "3 неверно, "
                word_3 = ""
            flash(flash_str[:-2])
    return render_template("quest_october_2025.html", word_1=word_1, word_2=word_2, word_3=word_3)