from web_app import app

from flask import redirect, url_for

@app.route("/", methods=["GET"])
def index_page():
    return redirect(url_for("auth_page"))