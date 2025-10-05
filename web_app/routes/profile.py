from flask import render_template

from web_app import app, Users


@app.route("/profile/<int:id>", methods=["GET"])
def get_profile(id):
    user = Users.get(Users.id == id)
    ranked_users = (
        Users
        .select()
        .where(Users.is_teacher == False)
        .order_by(Users.rating_points.desc(), Users.created_at.asc())
    )

    place = None
    for idx, u in enumerate(ranked_users, start=1):
        if u.id == user.id:
            place = idx
            break
    return render_template("profile.html", user=user, place=place)