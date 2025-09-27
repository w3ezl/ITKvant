from flask import request, jsonify, url_for
import os
from werkzeug.utils import secure_filename

from web_app import app

UPLOAD_FOLDER = os.path.join(app.static_folder, "uploads/avatars")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload_avatar", methods=["POST"])
def upload_avatar():
    code = request.args.get("code")
    if not code:
        return jsonify({"error": "No code provided"}), 400

    file = request.files.get("avatar")
    if not file:
        return jsonify({"error": "No file"}), 400

    # сохраняем строго с именем code.png
    filename = f"{secure_filename(code)}.png"
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    file.save(filepath)

    # генерируем URL для фронта
    url = url_for("static", filename=f"uploads/avatars/{filename}", _external=False)
    return jsonify({"url": url})