from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Person(db.Model,SerializerMixin):
    __tablename__ = 'persons'
    

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    origin = db.Column(db.String)
    email = db.Column(db.String)

    
    def __repr__(self):
         return f'<Person {self.name}, {self.age} years old, whose contact is {self.email} lives in {self.origin}>'