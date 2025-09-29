from flask import request, jsonify

from web_app import app
from web_app.routes._check_auth import is_login, current_user


@app.route('/update_status', methods=['POST'])
def update_status():
    if is_login():
        status = request.form.get('status', '').strip()
        user = current_user()
        user.status = status
        user.save()
        return jsonify({'message': 'OK'})
    return 403