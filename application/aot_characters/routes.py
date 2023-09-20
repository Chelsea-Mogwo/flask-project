from flask import jsonify, request
from werkzeug import exceptions
from application import app
from .controllers import index, show, create, update, delete

@app.route("/aot_characters/", methods= ["GET", "POST"])
def show_and_create():
    if request.method == "GET": return index()
    if request.method == "POST": return create()

@app.route("/aot_characters/<name>")
def show_character(name):
    return show(name)

@app.route("/aot_characters/<int:id>", methods=["PATCH", "DELETE"])
def update_and_delete(id):
    if request.method == "PATCH": return update(id)
    if request.method == "DELETE": return delete(id)


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"error": f"Opps {err}"}), 500

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error": f"Opps {err}"}), 404