import os
import shutil
from werkzeug.security import generate_password_hash

from web_app import app, db, models, Users, Achievements

db.connect()

tables = [
    models.Groups,
    models.Users,
    models.Projects,
    models.Achievements,
    models.RegistrationLinks,
    models.Tasks,
    models.UserAchievements,
    models.UserTasks
]

db.create_tables(tables, safe=True)

# Создание учителя, если нет
if not Users.select().where(Users.login == "w3ezl").exists():
    Users.create(
        login="w3ezl",
        password=generate_password_hash("(Kjkszpj0033)"),
        first_name="Павел",
        last_name="Николаев",
        father_name="Иванович",
        gender="male",
        is_teacher=True
    )

if not Achievements.select().where(Achievements.title == "Добро пожаловать!").exists():
    achiv = Achievements.create(
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
