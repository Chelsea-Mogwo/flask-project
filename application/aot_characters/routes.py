from flask import jsonify, request
from werkzeug import exceptions
from application import app
from .controllers import index

@app.route("/aot_characters", methods= ["GET"])
def show_and_create():
    if request.method == "GET": return index()

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"error": f"Opps {err}"}), 500