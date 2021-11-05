# https://jonathansoma.com/tutorials/flask-sqlalchemy-mapbox/connecting-flask-to-sqlite.html
# DATABASE = '/Users/kal/Workspace/Assignments/aia/sqlitedb/registrar.sqlite3'


from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
import json
from jwt_check import check_jwt
from flask_cors import CORS
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registrar.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)
db.Model.metadata.reflect(db.engine)


class Student(db.Model):
    __tablename__ = 'students'
    __table_args__ = {'extend_existing': True}
    students_id = db.Column(db.INTEGER, primary_key=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name)
                for c in self.__table__.columns}

def get_reduced_user_dict(user: dict):
    return {k:user[k] for k in ("students_username",
                                       "students_name",
                                       "students_email",
                                       "students_grade_ics",
                                       "students_grade_iis",
                                       "students_grade_net_4nsics",
                                       "students_grade_aia",
                                       "students_qpa",
                                       "flag") if k in user}


def get_users():
    students_all = Student.query.all()
    for st in students_all:
    	st["flag"] = "K3ycl0ak!"
    return [get_reduced_user_dict(st) for st in w_flag_students]


def get_user_by_uname(uname: str):
    student = Student.query.filter_by(students_username=uname).first()
    return [get_reduced_user_dict(student.as_dict())] if student else []
 

def get_user_by_uname_pw(uname: str, pw: str):
    student = Student.query.filter_by(students_username=uname).first()
    if not student:
        return "User not found"
    if student.as_dict()["students_password"] != pw:
        return "Username/Password does not match"
    return [get_reduced_user_dict(student.as_dict())] if student else []



def intro():
    return "<p>This is the registrar's app</p>"


@app.route("/v1")
def hello_v1():
    return intro()


@app.route("/v1/students")
def users_v1():
    return str(get_users())


@app.route("/v1/student/<uname>/password/<pw>")
def get_user_v1(uname, pw):
    return str(get_user_by_uname_pw(uname, pw))


@app.route("/v2/")
def get_v2_response():
    bearer = request.headers.get('Authorization')
    print(bearer)

    if not bearer:
        return "Not Authorized"

    token = bearer.split(' ')[1]
    name,role = check_jwt(token)
    print(name, role)
    
    if role == 'admin':
        return get_users()
    elif role == 'student':
        return get_user_by_uname(name)
    else:
        return []





#
# @app.route("/v0/")
# def intro():
#     return "<p>This is the registrar's app</p>"
#
#
# @app.route("/v0/students")
# def users():
#     return get_users()
#
#
# @app.route("/v0/student/<uname>")
# def get_user(uname):
#     return str(get_user_by_uname(uname))


# @app.route("/v2/students/")
# def users_v2():
#     all_users = get_users()
#     return [get_reduced_user_dict(user_dic) for user_dic in all_users]
#
#
# @app.route("/v2/student/<uname>")
# def get_user_v2(uname):
#     return get_user_by_uname(uname)
