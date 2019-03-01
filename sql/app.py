from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os 


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)

class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  

  def __init__(self, name): #constructor
    self.name = name
 

class StudentSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name')

student_schema = StudentSchema(strict=True)
student_schema = StudentSchema(many=True, strict=True)

@app.route('/student', methods=['POST'])
def add_student():
  name = request.json['name']
  new_student= Student(name)
  db.session.add(new_student)
  db.session.commit()
  return student_schema.jsonify(new_student)


@app.route('/student', methods=['GET'])
def get_students():
  all_students = Student.query.all()
  result = student_schema.dump(all_students)
  return jsonify(result.data)

@app.route('/student/<id>', methods=['PUT'])
def update_studentt(id):
  student = Student.query.get(id)
  name = request.json['name']
  student.name = name
  db.session.commit()
  return student_schema.jsonify(student)

@app.route('/student/<id>', methods=['DELETE'])
def delete_student(id):
  student = Student.query.get(id)
  db.session.delete(student)
  db.session.commit()

  return student_schema.jsonify(student)


class Course(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  

  def __init__(self, name): 
    self.name = name
 

class CourseSchema(ma.Schema):
  class Meta1:
    fields = ('id', 'name')

course_schema = CourseSchema(strict=True)
course_schema = CourseSchema(many=True, strict=True)

@app.route('/course', methods=['POST'])
def add_course():
  name = request.json['name']
  new_course= Course(name)
  db.session.add(new_course)
  db.session.commit()
  return course_schema.jsonify(new_course)


@app.route('/course', methods=['GET'])
def get_course():
  all_courses = Course.query.all()
  result = course_schema.dump(all_courses)
  return jsonify(result.data)

@app.route('/course/<id>', methods=['PUT'])
def update_course(id):
  course = Course.query.get(id)
  name = request.json['name']
  course.name = name
  db.session.commit()
  return course_schema.jsonify(course)

@app.route('/course/<id>', methods=['DELETE'])
def delete_course(id):
  course = Course.query.get(id)
  db.session.delete(course)
  db.session.commit()

  return course_schema.jsonify(course)

class Event(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  

  def __init__(self, name): 
    self.name = name
 

class EventSchema(ma.Schema):
  class Meta2:
    fields = ('id', 'name')

event_schema = EventSchema(strict=True)
event_schema = EventSchema(many=True, strict=True)

@app.route('/event', methods=['POST'])
def add_event():
  name = request.json['name']
  new_event= Event(name)
  db.session.add(new_event)
  db.session.commit()
  return event_schema.jsonify(new_event)


@app.route('/event', methods=['GET'])
def get_events():
  all_events = Event.query.all()
  result = event_schema.dump(all_events)
  return jsonify(result.data)

@app.route('/event/<id>', methods=['PUT'])
def update_event(id):
  event = Event.query.get(id)
  name = request.json['name']
  event.name = name
  db.session.commit()
  return event_schema.jsonify(event)

@app.route('/event/<id>', methods=['DELETE'])
def delete_event(id):
  event = Event.query.get(id)
  db.session.delete(event)
  db.session.commit()

  return event_schema.jsonify(event)