from flask import render_template, request, jsonify
from web_app import app
from web_app.models import Users, Groups
from web_app.routes._check_auth import is_admin

@app.route('/admin_rating')
def admin_rating():
    if not is_admin():
        return "Forbidden", 403

    groups = Groups.select().order_by(Groups.name)
    return render_template('dashboard/admin_rating.html', groups=groups)


@app.route('/admin_group_students')
def admin_group_students():
    if not is_admin():
        return jsonify({'error': 'Forbidden'}), 403

    group_id = request.args.get('group_id')
    if not group_id:
        return jsonify({'students': []})

    students = Users.select().where(
        (Users.group_id == group_id) & (Users.is_teacher == False)
    ).order_by(Users.last_name, Users.first_name)

    result = [{'id': s.id, 'first_name': s.first_name, 'last_name': s.last_name} for s in students]
    return jsonify({'students': result})


@app.route('/admin_student_rating')
def admin_student_rating():
    if not is_admin():
        return jsonify({'error': 'Forbidden'}), 403

    student_id = request.args.get('student_id')
    student = Users.get_or_none(Users.id == student_id)
    if not student:
        return jsonify({'points': 0})

    return jsonify({'points': student.rating_points})


@app.route('/admin_save_rating', methods=['POST'])
def admin_save_rating():
    if not is_admin():
        return jsonify({'success': False, 'error': 'Forbidden'}), 403

    student_id = request.form.get('student_id')
    points = request.form.get('points')

    if not student_id or points is None:
        return jsonify({'success': False, 'error': 'Invalid data'}), 400

    student = Users.get_or_none(Users.id == student_id)
    if not student:
        return jsonify({'success': False, 'error': 'Student not found'}), 404

    try:
        student.rating_points = int(points)
        student.save()
    except ValueError:
        return jsonify({'success': False, 'error': 'Invalid points'}), 400

    return jsonify({'success': True})
