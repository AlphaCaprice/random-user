import requests
import random

from db_classes import Person
from app import db, jsonify


def write_people_to_db(number=10):
    """Download given number of users from randomuser.me and save up to
    5 users in data base, that don't have 'r' symbol in first and last name.

    Args:
        number: a number of random users to download

    Returns:
        int: number of users, that have been saved in data base
    """
    params = f"?results={number}&inc=gender,name,location,email,login"
    url = f"https://randomuser.me/api/{params}"

    max_people_to_db = 5
    while max_people_to_db:
        people = requests.get(url).json()

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


def random_user_from_db() -> dict:
    qry_all_people = Person.query.all()
    random_person_number = random.randint(0, len(qry_all_people)-1)
    return qry_all_people[random_person_number].serialize

def one_more_new_function():
    ...
