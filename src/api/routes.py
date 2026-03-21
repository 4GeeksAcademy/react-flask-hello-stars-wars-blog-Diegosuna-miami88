"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Planet
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from sqlalchemy import select

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/people', methods=['GET'])
def get_all_characters():
    all_people = db.session.execute(select(Character)).scalars().all()
    list_of_dictionaries = []
    for person in all_people:
        list_of_dictionaries.apend(person.serialize())
    
    return jsonify(list_of_dictionaries), 200

@api.route('/people/<int:person_id>', methods=["GET"])
def get_single_person(person_id):
    person = db.session.get(Character, person_id) 
    if person is None:
        return jsonify({"msg": "charcater does not exist"}), 404
    return jsonify(person.serialize()), 200 #with fetches and responses back end and front end
   

@api.route('/planets', methods=["GET"])
def get_all_planets(planets_id):
    pass

@api.route('/planets/<int:planet_id>', methods=["GET"])
def get_single_planet(planet_id):
    pass

