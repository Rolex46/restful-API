from flask import Flask, request, Blueprint,jsonify, make_response
from flask_restful import Api, Resource
from flask_migrate import Migrate
from models import db, Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///persons.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


migrate = Migrate(app, db)
db.init_app(app)

# api = Api(app)
api = Blueprint('api', __name__)

# class Home(Resource):
#     def get(self):
#         response_dict = {
#             "index":"Welcome to the Person restful API"
#         }

#         response = make_response(
#             jsonify(response_dict),200
#         )
#         return response
    
# api.add_resource(Home,'/')

# class Persons(Resource):
#     def get(self):
#         person_dict = [person.to_dict() for person in Person.query.all()]
#         response = make_response(
#             jsonify(person_dict),200
#         )
#         return response
    
#     def post(self):
#         data = request.form.get()
#         person = Person(
#             name = data['name'],
#             age = data['age'],
#             origin = data['origin'],
#             email = data['email']
#         )
#         db.session.add(person)
#         db.sesison.commit()
#         response_dict = person.to_dict()
#         response = make_response(
#             jsonify(response_dict),201
#         )
#         return response

    
# api.add_resource(Persons,'/api')

# class PersonsById(Resource):
#     def get(self, id):
#         person = Person.query.filter_by(id=id).first()
#         response_dict = person.to_dict()
#         response = make_response(
#             jsonify(response_dict),200
#         )
#         return response
    
#     def patch(self, id):
#         person = Person.query.filter_by(id=id).first()
#         for attr in request.form:
#             setattr(person, attr,request.form[attr])
        
#         db.session.add(person)
#         db.session.commit()

#         response_dict = person.to_dict()

#         response = make_response(
#             jsonify(response_dict),200
#         )
#         return response
    
#     def delete(self,id):
#         record = Person.query.filter_by(id=id).first()
#         db.session.delete(record)
#         db.session.commit()
#         response_dict = {"message": "record successfully deleted"}

#         response = make_response(
#             jsonify(response_dict),
#             200
#         )

#         return response
    
# api.add_resource(PersonsById,'/api/<int:id>')

# class PersonsByName(Resource):
#     def get(self, name):
#         person = Person.query.filter_by(name=name).first()
#         response_dict = person.to_dict()
#         response = make_response(
#             jsonify(response_dict),200
#         )
#         return response
    
#     def patch(self,name):
#         record = Person.query.filter_by(name=name).first()

#         for attr in request.form:
#             setattr(record, attr, request.form[attr])
#         db.session.add(record)
#         db.session.commit()

#         response_dict = record.to_dict()
#         response = make_response(
#             jsonify(response_dict),200
#         )
#         return response
    
#     def delete(self, name):
#         record = Person.query.filter_by(name=name).first()
#         db.session.delete(record)
#         db.session.commit()

#         response_dict = {
#             "message": "record deleted successfully"
#         }
#         response = make_response(
#             jsonify(response_dict),200
#         )
#         return response

# api.add_resource(PersonsByName,'/api/<string:name>')
@app.route('/api', methods=['GET'])
def test():
    if request.method == 'GET':
        return jsonify({"response": " Get request called"})

@api.route('/api', methods=['POST'])
def create_person():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': '"name" is required'}), 400

    new_person = Person(name=data['name'])
    db.session.add(new_person)
    db.session.commit() #commit session

    return jsonify({'message': 'Person created successfully', 'person_id': new_person.id})

@api.route('/api/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = Person.query.get(person_id)
    if person is None:
        return jsonify({'error': 'Person not found'}), 404
    return jsonify({'id': person.id, 'name': person.name})

@api.route('/api/<int:person_id>', methods=['PUT', 'PATCH'])
def update_person(person_id):
    data = request.get_json()
    person = Person.query.get(person_id) #query database
    if person is None:
        return jsonify({'error': 'Person not found'}), 404

    if 'name' not in data:
        return jsonify({'error': '"name" is required'}), 400

    person.name = data['name']
    db.session.commit()
    return jsonify({'message': 'Person updated successfully', 'person_id': person.id})

@api.route('/api/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = Person.query.get(person_id)
    if person is None:
        return jsonify({'error': 'Person not found'}), 404

    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted successfully'})


#register api blueprint with flask
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(port=5555)