import pprint
import json
import requests
import random

from flask_server.db_classes import Person
from flask_server.app import db, jsonify


def get_people(number: int):
    params = f"?results={number}&inc=gender,name,location,email,login"
    url = f"https://randomuser.me/api/{params}"
    people = requests.get(url).json()

    max_people_to_db = 5
    for person in people['results']:
        if not max_people_to_db:
            break

        first_name = person['name']['first']
        last_name = person['name']['last']
        if not ('r' in first_name.lower() or 'r' in last_name.lower()):
            street = "{number} {name}".format(**person['location']['street'])
            city_state = "{city} {state}".format(**person['location'])

            # create record in data base
            db_person = Person(id=person['login']['uuid'],
                               gender=person['gender'],
                               first_name=first_name,
                               last_name=last_name,
                               location=f"{street} {city_state}",
                               email=person['email'])
            db.session.add(db_person)
            print(f"Person {first_name} {last_name } has been written to db!")
            max_people_to_db -= 1
    db.session.commit()
    qry_all_people = Person.query.all()
    random_person_number = random.randint(0, len(qry_all_people)-1)
    return qry_all_people[random_person_number].serialize
