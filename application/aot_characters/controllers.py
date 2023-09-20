from .models import Character
from werkzeug import exceptions
from flask import jsonify, request
from .. import db

def index():
    try:
        characters = Character.query.all()
        data = [c.json for c in characters]
        return jsonify({"characters": data})
    except:
        raise exceptions.InternalServerError("We are working on it")
    
def show(name):
    try:
        c = Character.query.filter_by(firstname=name.capitalize()).first()
        # print(c.json)
        return jsonify({"data": c.json}), 200
    except:
        raise exceptions.NotFound("Character doesn't exist")