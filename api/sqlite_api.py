# https://jonathansoma.com/tutorials/flask-sqlalchemy-mapbox/connecting-flask-to-sqlite.html
# DATABASE = '/Users/kal/Workspace/Assignments/aia/sqlitedb/registrar.sqlite3'


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registrar.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)


class Student(db.Model):
    __tablename__ = 'students'
    __table_args__ = {'extend_existing': True}
    students_id = db.Column(db.INTEGER, primary_key=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name)
                for c in self.__table__.columns}


def get_users():
    students_all = Student.query.all()
    retval = [student.as_dict() for student in students_all]
    return str(retval)

def get_user_by_uname(uname: str):
    student = Student.query.filter_by(students_username=uname).first()
    return str(student.as_dict())


def get_user_by_uname_pw(uname: str, pw: str):
    student = Student.query.filter_by(students_username=uname).first()
    if not student:
        return "User not found"
    if student.as_dict()["students_password"] != pw:
        return "Username/Password does not match"
    return str(student.as_dict())



@app.route("/v0/")
def intro():
    return "<p>This is the registrar's app</p>"


@app.route("/v0/students")
def users():
    return get_users()


@app.route("/v0/student/<uname>")
def get_user(uname):
    return get_user_by_uname(uname)


@app.route("/v1")
def hello_v1():
    return intro()


@app.route("/v1/students")
def users_v1():
    return get_users()


@app.route("/v1/student/<uname>/password/<pw>")
def get_user_v1(uname, pw):
    return get_user_by_uname_pw(uname, pw)

@app.route("/v2/")
def intro_v2():
    return intro()


@app.route("/v2/students/")
def users_v2():
    return get_users()


@app.route("/v2/student/<uname>")
def get_user_v2(uname):
    return get_user_by_uname(uname)
