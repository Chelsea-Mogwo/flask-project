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
        c = Character.query.filter_by(firstname=name.capitalize()).first() or Character.query.filter_by(lastname=name.capitalize()).first()
        return jsonify({"data": c.json}), 200
    except:
        raise exceptions.NotFound("Character doesn't exist")

def create():
    try:
        firstname, lastname, age, occupation = request.json.values()
        new_c = Character(firstname=firstname, lastname=lastname, age=age, occupation=occupation)
        db.session.add(new_c)
        db.session.commit()
        return jsonify({"data": new_c.json}), 201
    except:
        raise exceptions.InternalServerError(f"We cannot process your request. age, firstname, lastname and occupation are required and you only provided {new_c}")

def update(id):
    data = request.json
    c = Character.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(c, attribute):
            setattr(c, attribute, value)
    db.session.commit()
    return jsonify({"data": c.json})

def delete(id):
    c = Character.query.filter_by(id=id).first()
    db.session.delete(c)
    db.session.commit()
    return f"Character Deleted", 204