from werkzeug.security import generate_password_hash
from web_app import app, Users


def change_user_password():
    print("=== Смена пароля пользователя ===")

    try:
        user_id = input("Введите ID пользователя: ").strip()
        if not user_id:
            print("Ошибка: ID пользователя не может быть пустым")
            return

        user_id = int(user_id)

        with app.app_context():
            try:
                user = Users.get(Users.id == user_id)
            except Users.DoesNotExist:
                print(f"Ошибка: Пользователь с ID {user_id} не найден")
                return

            print(f"\nНайден пользователь:")
            print(f"ID: {user.id}")
            print(f"Логин: {user.login}")
            print(f"Имя: {user.first_name} {user.last_name}")
            print(f"Группа: {user.group.name}")

            new_password = input("\nВведите новый пароль: ").strip()
            if not new_password:
                print("Ошибка: Пароль не может быть пустым")
                return

            if len(new_password) < 6:
                print("Ошибка: Пароль должен быть не менее 6 символов")
                return

            confirm = input("Вы уверены, что хотите изменить пароль? (y/N): ").strip().lower()
            if confirm not in ['y', 'yes', 'д', 'да']:
                print("Отменено")
                return

            user.password = generate_password_hash(new_password)
            user.save()

            print("✅ Пароль успешно изменен!")

    except ValueError:
        print("Ошибка: ID пользователя должен быть числом")
    except KeyboardInterrupt:
        print("\n\nОтменено пользователем")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    change_user_password()