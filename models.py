import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']
# database_name = "casting"
# database_path = "postgres://{}:{}@{}/{}".format(
#     'postgres', , 'localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have
    multiple verisons of a database
'''
# def db_drop_and_create_all():
#     db.drop_all()
#     db.create_all()


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    title = Column(String(90), unique=True)
    release = Column(String(180), nullable=False)

    def __init__(self, title, release):
        self.title = title
        self.release = release

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release': self.release
        }


class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    name = Column(String(80))
    age = Column(Integer)
    gender = Column(String(30))

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }
