import os
import shutil
from werkzeug.security import generate_password_hash

from web_app import app, db, models, User, Achievement

db.connect()

tables = [
    models.Group,
    models.User,
    models.Project,
    models.Achievement,
    models.RegistrationLink,
    models.Task,
    models.UserAchievement,
    models.UserTask
]

db.create_tables(tables, safe=True)

# Создание учителя, если нет
if not User.select().where(User.login == "w3ezl").exists():
    User.create(
        login="w3ezl",
        password=generate_password_hash("(Kjkszpj0033)"),
        first_name="Павел",
        last_name="Николаев",
        father_name="Иванович",
        gender="male",
        is_teacher=True
    )

if not Achievement.select().where(Achievement.title == "Добро пожаловать!").exists():
    achiv = Achievement.create(
        title="Добро пожаловать!",
        description="Зарегистрируйтесь в сервисе"
    )

    icon_folder = os.path.join(app.static_folder, "uploads", "achiv_icons")
    os.makedirs(icon_folder, exist_ok=True)

    default_icon = os.path.join(icon_folder, "default.png")
    new_icon = os.path.join(icon_folder, f"{achiv.id}.png")
    if os.path.exists(default_icon):
        shutil.copy(default_icon, new_icon)

    achiv.icon = f"uploads/achiv_icons/{achiv.id}.png"
    achiv.save()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
