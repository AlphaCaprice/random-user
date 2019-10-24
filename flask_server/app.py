from pathlib import Path


from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import random_user_module as rum
import db_classes

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_files/people.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')


@app.route("/process_data/", methods=['POST'])
def download_random_user():
    data = request.get_json()
    try:
        number_of_people = int(data['number'])
    except ValueError:
        return {'answer': 'input value is not number'}

    print(number_of_people)
    number_of_saved = rum.write_people_to_db(number_of_people)
    data = jsonify({'answer': number_of_saved})
    return data


@app.route("/random_user/", methods=['POST'])
def return_random_user():
    person = rum.random_user_from_db()
    return render_template('index.html', person=person)


if __name__ == "__main__":
    if not (Path("db_files/people.db")).exists():
        db_classes.create_data_base()
    app.run(host='0.0.0.0')
