from flask import render_template

from web_app import app, User


@app.route("/profile/<int:id>", methods=["GET"])
def get_profile(id):
    user = User.get(User.id == id)
    ranked_users = (
        User
        .select()
        .where(User.is_teacher == False)
        .order_by(User.rating_points.desc(), User.id.asc())
    )

    place = None
    for idx, u in enumerate(ranked_users, start=1):
        if u.id == user.id:
            place = idx
            break
    return render_template("profile.html", user=user, place=place)