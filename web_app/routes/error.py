from flask import render_template
from pyexpat.errors import messages

from web_app import app


@app.errorhandler(404)
@app.errorhandler(500)
@app.errorhandler(403)
@app.errorhandler(505)
def handle_errors(e):
    code = getattr(e, 'code', 500)
    if code == 404:
        message = "Такой страницы не существует. Если она была - значит удалили, если не было - зачем вы вообще сюда зашли? В любом случае, никак не могу тебе помочь("
    elif code == 403:
        message = "Ну смотри, тут либо прав не хватает, либо ты не зарегистрирован. Проверь все повнимательнее и попробуй еще раз)"
    elif code == 500:
        message = "Ошибка на стороне сервера. Скорее всего программист намутил что-то и сделал все неправильно. Не переживайте, скорее всего ошибку уже увидели и будут исправлять("
    else:
        message = e.description
    return render_template('error.html', code=code, message=message), code