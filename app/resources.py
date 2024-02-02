from flask_restx import Resource, Namespace
from models import *
from api_models import course_model,course_post_model, student_model, student_post_model

ns = Namespace("api")

@ns.route('/hello')
class hello(Resource):
    def get(self):
        return {'message':'hello from restx'}
    
@ns.route('/courses')
class CoursesListApi(Resource):
    @ns.marshal_list_with(course_model)
    def get(self):
        return Course.query.all()
    
    @ns.expect(course_post_model)
    @ns.marshal_with(course_model)
    def post(self):
        course = Course(name=ns.payload['name'])
        db.session.add(course)
        db.session.commit()
        return course,201

@ns.route('/courses/<int:id>')
class CourseApi(Resource):
    @ns.marshal_with(course_model)
    def get(self, id):
        course = Course.query.get(id)
        return course

    @ns.expect(course_post_model)
    @ns.marshal_with(course_model)
    def put(self, id):
        course = Course.query.get(id)
        course.name = ns.payload['name']
        db.session.commit()
        return course
    
    def delete(self,id):
        course = Course.query.get(id)
        db.session.delete(course)
        db.session.commit()
        return {'message':'Course removed successfully'},204

    
@ns.route('/students')
class StudentsListApi(Resource):
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()
    
    @ns.expect(student_post_model)
    @ns.marshal_with(student_model)
    def post(self):
        student = Student(name=ns.payload['name'],course_id=ns.payload['course_id'])
        db.session.add(student)
        db.session.commit()
        return student,201
    

@ns.route('/students/<int:id>')
class StudentsApi(Resource):
    @ns.marshal_with(student_model)
    def get(self, id):
        student = Student.query.get(id)
        return student

    @ns.expect(student_post_model)
    @ns.marshal_with(student_model)
    def put(self, id):
        student = Student.query.get(id)
        student.name = ns.payload['name']
        student.course_id = ns.payload['course_id']
        db.session.commit()
        return student
    
    def delete(self,id):
        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()
        return {'message':'Student removed successfully'},204