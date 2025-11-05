import json
import os
from urllib.parse import unquote

from web_app import app, Users
from web_app.routes._check_auth import is_login, current_user

from flask import redirect, url_for, render_template, abort, current_app

def month_year_key(filename):
    MONTHS_RU = {
        "Январь": 1,
        "Февраль": 2,
        "Март": 3,
        "Апрель": 4,
        "Май": 5,
        "Июнь": 6,
        "Июль": 7,
        "Август": 8,
        "Сентябрь": 9,
        "Октябрь": 10,
        "Ноябрь": 11,
        "Декабрь": 12
    }
    name = filename.replace(".json", "")
    month_str, year_str = name.split(" ")
    month = MONTHS_RU.get(month_str, 0)
    year = int(year_str)
    return (year, month)

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

@app.route("/rating_archive/<name>")
def rating_archive(name):
    name = unquote(name)
    path = os.path.join(current_app.static_folder, "rating_history", f"{name}.json")

    if not os.path.exists(path):
        abort(404)

    with open(path, encoding="utf-8") as f:
        raw = json.load(f)

    data = []
    for r in raw:
        try:
            user = Users.get(Users.id == r["user_id"])
            data.append({"user": user, "rating": r["rating"]})
        except Users.DoesNotExist:
            pass

    data.sort(key=lambda x: x["rating"], reverse=True)
    return render_template("dashboard/rating_archive.html", data=data, file_name=name)

@app.route("/rating_list")
def rating_list():
    history_dir = os.path.join(current_app.static_folder, "rating_history")

    if not os.path.exists(history_dir):
        return json.dumps([])

    files = [f for f in os.listdir(history_dir) if f.endswith(".json")]

    files.sort(key=month_year_key, reverse=True)
    return json.dumps(files, ensure_ascii=False)


@app.route("/admin", methods=["GET"])
def admin():
    if not is_login():
        return redirect(url_for("auth_page"))
    if not current_user().is_teacher:
        abort(403)
    return render_template("dashboard/admin.html")