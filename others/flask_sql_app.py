from flask import Flask
from flask_sqlalchemy import SQLAlchemy as Sql
import MySQLdb

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootpassword@127.0.0.1:3306/registrar'
db = Sql(app)


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    phone = db.Column(db.String(100))
    email = db.Column(db.String(255))
    postal_zip = db.Column(db.String(10))
    country = db.Column(db.String(100))
    grade_letter = db.Column(db.String(10))
    grade_percent = db.Column(db.Integer)
    password = db.Column(db.String(255))

    def __init__(self, id, name, phone, email, postal_zip,
                 country, grade_letter, grade_percent, password):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.postal_zip = postal_zip
        self.country = country
        self.grade_letter = grade_letter
        self.grade_percent = grade_percent
        self.password = password


print(Students.query.all())





