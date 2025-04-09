from flask import Flask, render_template
from database import db
from models import Student
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def students_list():
    with app.app_context():
        students = Student.query.order_by(Student.name).all()
        return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)