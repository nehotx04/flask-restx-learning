from extensions import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(255),unique= True)
    students = db.relationship("Student", back_populates="course")

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(255),unique= True)
    course_id = db.Column(db.ForeignKey("course.id"))
    course = db.relationship("Course", back_populates="students")
