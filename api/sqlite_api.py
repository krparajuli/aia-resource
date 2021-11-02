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


def get_users():
    students_all = Student.query.all()
    retval = [student.as_dict() for student in students_all]
    return str(retval)

def get_user_by_uname(uname: str):
    student = Student.query.filter_by(students_username=uname).first()
    return json.dumps(student.as_dict())
   


def get_user_by_uname_pw(uname: str, pw: str):
    student = Student.query.filter_by(students_username=uname).first()
    if not student:
        return "User not found"
    if student.as_dict()["students_password"] != pw:
        return "Username/Password does not match"
    return student.as_dict()

def get_name_and_grades(uname: str, pw: str):
    user = get_user_by_uname_pw(uname, pw)
    ret_dict = {}
    ret_dict["username"] = user["students_username"]
    ret_dict["name"]  =  user["students_name"]
    ret_dict["email"] = user["students_email"]
    ret_dict["grade_ics"] = user["students_grade_ics"]
    ret_dict["grade_iis"] = user["students_grade_iis"]
    ret_dict["grade_net_4ns"] = user["students_grade_net_4nsics"]
    ret_dict["grade_aia"] = user["students_grade_aia"]
    ret_dict["qpa"] = user["students_qpa"]
    return ret_dict



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
    return get_name_and_grades(uname, pw)

@app.route("/v2/")
def intro_v2():
    bearer  = request.headers.get('Authorization')
    print(bearer)
    if(bearer == None):
    	return "Not Authorized"
    token = bearer.split(' ')[1]
    ans = check_jwt(token)
    print(ans)
    return get_user_by_uname(ans)


@app.route("/v2/students/")
def users_v2():
    return get_users()


@app.route("/v2/student/<uname>")
def get_user_v2(uname):
    return get_user_by_uname(uname)
