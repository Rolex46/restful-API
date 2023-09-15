from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Person(db.Model,SerializerMixin):
    __tablename__ = 'persons'
    

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    origin = db.Column(db.String)
    email = db.Column(db.String)

    @validates('name')
    def validate_name(self,key,name):
        if not isinstance(name, str):
            raise ValueError('Name must be a string')
        return name
    
    @validates('age')
    def validate_age(self,key,age):
        if not isinstance(age,int):
            raise ValueError('age must be a number')
        return age
    
    @validates('origin')
    def validate_name(self,key,origin):
        if not isinstance(origin, str):
            raise ValueError('origin must be a string')
        return origin
         
    @validates('email')
    def validate_email(self, key, address):
        if '@' not in address:
            raise ValueError("failed simple email validation")
        return address        

    
    def __repr__(self):
         return f'<Person {self.name}, {self.age} years old, whose contact is {self.email} lives in {self.origin}>'