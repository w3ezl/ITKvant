from web_app import app

from flask import redirect, url_for, render_template

from web_app.routes._check_auth import is_login


@app.route("/auth")
def auth_page():
    if not is_login():
        return render_template("auth.html")
    return redirect(url_for("dashboard_page"))