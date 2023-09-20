from flask import jsonify, request
from werkzeug import exceptions
from application import app
from .controllers import index, show

@app.route("/aot_characters", methods= ["GET"])
def show_and_create():
    if request.method == "GET": return index()

@app.route("/aot_characters/<name>", methods=["GET"])
def find_character(name):
    if request.method == "GET": return show(name)


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"error": err}), 500

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error": err}), 404