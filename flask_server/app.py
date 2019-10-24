from pathlib import Path


from flask import Flask, render_template, jsonify, request, redirect, url_for, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from flask_server import random_user_module as rum
from flask_server import db_classes

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
def get_random_user():
    data = request.get_json()
    try:
        number_of_people = int(data['number'])
    except ValueError:
        return {'answer': 'input value is not number'}

    print(number_of_people)
    person = rum.get_people(number_of_people)
    data = jsonify(person)
    return data


if __name__ == "__main__":
    if not (Path("/db_files/people.db")).exists():
        db_classes.create_data_bases()

    app.run(host='0.0.0.0', debug=True)
    # rum.get_people(1)
