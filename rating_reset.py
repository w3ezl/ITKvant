import os, json
from datetime import datetime
from web_app import  app, Users, db

with app.app_context():
    history_dir = os.path.join(app.static_folder, "rating_history")
    os.makedirs(history_dir, exist_ok=True)

    name = input("Введите название архива: ").strip()
    if not name:
        name = datetime.now().strftime("%Y-%m-%d_%H-%M")

    filename = os.path.join(history_dir, f"{name}.json")

    users = Users.select().where(Users.is_teacher == False).order_by(Users.rating_points.desc())

    data = [{"user_id": u.id, "rating": u.rating_points} for u in users]

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    with db.atomic():
        (Users
         .update(rating_points=0)
         .where(Users.is_teacher == False)
         .execute())

    print("✅ Архив создан:", filename)
    print("✅ Рейтинг учеников обнулён")
