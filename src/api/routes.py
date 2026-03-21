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
        return jsonify({"msg": "Charcater does not exist"}), 404
    return jsonify(person.serialize()), 200 #with fetches and responses back end and front end
   

@api.route('/planets', methods=["GET"])
def get_all_planets(planet):
    all_planets = db.session.execute(select(Planet)).scalars().all()
    list_of_dictionaries = []
    for person in all_planets:
        list_of_dictionaries.apend(person.serialize())
    return jsonify(list_of_dictionaries), 200
   

@api.route('/planets/<int:planet_id>', methods=["GET"])
def get_single_planet(planet_id):
    planet = db.session.get(planet_id)
    if planet is None:
        return jsonify({"msg":" Planet deos not exist"}), 404
    return jsonify(planet_id.serialize()), 200
    

@api.route('/users', methods=['GET'])
def get_all_users(users):
    user = db.session.get(users)
    if user is None:
        return jsonify({"msg":" User deos not exist"}), 404
    return jsonify(users.serialize()), 200
    
@api.route('/users/<int:user_id>/favorites', methods=['GET'])
def add_user_favorites(user_id):
    pass

@api.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    pass

@api.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    pass

@api.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_person(people_id):
    pass

@api.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_person(people_id):
    pass


#@api.route('/users/favorites', methods=["GET"])
#def get_all_favorites(favorites):
 #   favorite = db.session.get(favorites)
  #  if favorite is None:
   #     return jsonify({"msg": "Favorite does not exist"}), 404
    #return jsonify(favorite.serialize()),200
    



#@api.route('/favorite/people/<int:people_id>', methods=['POST'])
#def add_favorite_person(people_id):
    #pass



#@api.route('/favorite/people/<int:people_id>', methods=['DELETE'])
#def delete_favorite_person(people_id):
    #pass

