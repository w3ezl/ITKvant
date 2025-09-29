from flask import request, jsonify
import os
from web_app import app
from web_app.routes._check_auth import is_login, current_user

@app.route('/update_avatar', methods=['POST'])
def update_avatar():
    if not is_login():
        return jsonify({'error': 'Unauthorized'}), 403

    file = request.files.get('avatar')
    if not file:
        return jsonify({'error': 'No file'}), 400

    filename = f"{current_user().id}.png"
    path = os.path.join(app.static_folder, 'uploads/avatars', filename)
    file.save(path)
    return jsonify({'url': f"/static/uploads/avatars/{filename}"})