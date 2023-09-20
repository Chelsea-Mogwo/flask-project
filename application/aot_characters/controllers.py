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