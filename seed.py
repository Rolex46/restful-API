import random
from faker import Faker
from app import app
from models import db, Person

with app.app_context():
    fake = Faker()

    Person.query.delete()

    persons = []

    for i in range(1,10):
        p = Person(
            name = fake.name(),
            age = random.randint(10,40),
            origin = fake.country(),
            email = fake.email()
        )
        persons.append(p)
    db.session.add_all(persons)
    db.session.commit()
 