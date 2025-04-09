from app import app
from database import db
from models import Student


def create_sample_data():
    with app.app_context():
        db.create_all()

        students = [
            Student(name="Глеб Латышев", gender="М", age=17,
                    hair_color="Русый", eye_color="Голубые"),
            Student(name="Мария Петрова", gender="Ж", age=102,
                    hair_color="Брюнетка", eye_color="Карие"),
            Student(name="Алексей Сидоров", gender="М", age=100,
                    hair_color="Шатен", eye_color="Зеленые")
        ]

        db.session.add_all(students)
        db.session.commit()
        print("Данные студентов добавлены!")


if __name__ == '__main__':
    create_sample_data()