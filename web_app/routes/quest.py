from flask import render_template, redirect, url_for, flash, request, abort

from web_app import app, UserQuests, UserAchievements, Achievements
from web_app.routes._check_auth import is_login, current_user


@app.route("/october_2025", methods=["GET"])
def page_quest_10_2025():
    if not is_login():
        return redirect(url_for("auth_page"))

    user = current_user()

    # Проверяем, прошел ли уже текущий пользователь квест
    user_completed = UserQuests.select().where(
        (UserQuests.user == user) &
        (UserQuests.quest_name == "october_2025")
    ).exists()

    if user_completed:
        abort(404)
    return render_template("quest_october_2025.html", word_1="", word_2="", word_3="")


@app.route("/october_2025", methods=["POST"])
def post_quest_10_2025():
    if not is_login():
        return redirect(url_for("auth_page"))

    user = current_user()

    user_completed_quest = UserQuests.select().where(
        (UserQuests.user == user) &
        (UserQuests.quest_name == "october_2025")
    ).exists()

    user_has_achiv = UserAchievements.select().where(
        (UserAchievements.user == user) &
        (UserAchievements.achievement == Achievements.get(Achievements.title == "Криптограф Цезаря"))
    ).exists()

    if user_completed_quest or user_has_achiv:
        abort(404)

    word_1 = request.form.get("word_1")
    word_2 = request.form.get("word_2")
    word_3 = request.form.get("word_3")

    if word_1.lower() == "кванториум" and word_2.lower() == "маяковский" and word_3.lower() == "цезарь":
        user.rating_points += 5
        user.save()

        UserQuests.create(user=user, quest_name="october_2025")
        return render_template("quest_october_2025_completed.html")
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