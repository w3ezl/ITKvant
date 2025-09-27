from flask import request, url_for, render_template
from werkzeug.utils import redirect

from web_app import app, Group, User
from web_app.routes._check_auth import is_login, current_user


@app.route("/group/<int:id>", methods=["GET"])
def get_group(id):
    group = Group.get(Group.id == id)
    return render_template("group.html", group=group)

@app.route("/group/<int:id>", methods=["DELETE"])
def delete_group(id):
    group = Group.get(Group.id == id)
    group.delete_instance()
    return ("", 204)

@app.route("/group/form", methods=["GET"])
def form_group():
    if not is_login():
        return redirect(url_for("auth_page"))
    if not current_user().is_teacher:
        return 404
    if request.args.get("id"):
        group = Group.get(Group.id == int(request.args.get("id")))
    else:
        group = {}
    teachers = User.select().where(User.is_teacher == True)
    return render_template("group_form.html", teachers=teachers, group=group)

@app.route("/group", methods=["POST"])
def create_group():
    if not is_login():
        return redirect(url_for("auth_page"))
    if not current_user().is_teacher:
        return 404
    name = request.form.get("name")
    year = int(request.form.get("year"))
    teacher_id = int(request.form.get("teacher"))
    schedule = {}

    for key, value in request.form.items():
        if key.startswith("schedule_"):
            day = key.replace("schedule_", "")
            if day not in schedule:
                schedule[day] = []
            schedule[day].append(value)

    if request.args.get("id"):
        group = Group.get(Group.id == int(request.args.get("id")))
        group.name = name
        group.study_year = year
        group.teacher_id = User.get(User.id == teacher_id)
        group.schedule = schedule
        group.save()
    else:
        Group.create(
            name=name,
            study_year=year,
            teacher_id=User.get(User.id == teacher_id),
            schedule=schedule
        )

    return redirect(url_for("dashboard_page", page="admin", select="groups"))
