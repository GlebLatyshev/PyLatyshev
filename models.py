from database import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    hair_color = db.Column(db.String(20))
    eye_color = db.Column(db.String(20))

    def __repr__(self):
        return f'<Student {self.name}>'