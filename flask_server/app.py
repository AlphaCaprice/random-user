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


@app.route("/", methods=['POST', 'GET'])
def index():
    person = rum.random_user_from_db()
    return render_template('index.html', person=person)


if __name__ == "__main__":
    if not (Path("db_files/people.db")).exists():
        db_classes.create_data_base()
    if len(db_classes.Person.query.all()) < 5:
        rum.write_people_to_db()

    app.run(host='0.0.0.0', port=5000)
