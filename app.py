from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource
from flask_migrate import Migrate
from models import db, Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///persons.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Home(Resource):
    def get(self):
        response_dict = {
            "index":"Welcome to the Person restful API"
        }

        response = make_response(
            jsonify(response_dict),200
        )
        return response
    
api.add_resource(Home,'/api')

class Persons(Resource):
    def get(self):
        person_dict = [person.to_dict() for person in Person.query.all()]
        response = make_response(
            jsonify(person_dict),200
        )
        return response
    
    def post(self):
        new_person = Person(
            name = request.form['name'],
            age = request.form['age'],
            origin = request.form['origin'],
            email = request.form['email'],
        )
        db.session.add(new_person)
        db.session.commit()
        response_dict = new_person.to_dict()

        response = make_response(
            jsonify(response_dict),201
        )
        return response
    
api.add_resource(Persons, '/api/persons')

class PersonsById(Resource):
    def get(self, id):
        person = Person.query.filter_by(id=id).first()
        response_dict = person.to_dict()
        response = make_response(
            jsonify(response_dict),200
        )
        return response
    
    def patch(self, id):
        person = Person.query.filter_by(id=id).first()
        for attr in request.form:
            setattr(person, attr,request.form[attr])
        
        db.session.add(person)
        db.session.commit()

        response_dict = person.to_dict()

        response = make_response(
            jsonify(response_dict),200
        )
        return response
    
    def delete(self,id):
        record = Person.query.filter_by(id=id).first()
        db.session.delete(record)
        db.session.commit()
        response_dict = {"message": "record successfully deleted"}

        response = make_response(
            jsonify(response_dict),
            200
        )

        return response
    
api.add_resource(PersonsById,'/api/persons/<int:id>')

class PersonsByName(Resource):
    def get(self, name):
        person = Person.query.filter_by(name=name).first()
        response_dict = person.to_dict()
        response = make_response(
            jsonify(response_dict),200
        )
        return response
    
    def patch(self,name):
        record = Person.query.filter_by(name=name).first()

        for attr in request.form:
            setattr(record, attr, request.form[attr])
        db.session.add(record)
        db.session.commit()

        response_dict = record.to_dict()
        response = make_response(
            jsonify(response_dict),200
        )
        return response
    
    def delete(self, name):
        record = Person.query.filter_by(name=name).first()
        db.session.delete(record)
        db.session.commit()

        response_dict = {
            "message": "record deleted successfully"
        }
        response = make_response(
            jsonify(response_dict),200
        )
        return response

api.add_resource(PersonsByName,'/api/persons/<string:name>')

if __name__ == '__main__':
    app.run(port=5555)