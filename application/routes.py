from application import app
from flask import jsonify

@app.route("/")
def hello_world():
    return jsonify({
        "message": "Welcome",
        "description": "Attack on Titan Characters API",
        "endpoints": [
            "GET/",
            "POST/",
            "PATCH/",
            "DELETE/",
        ]
    }), 200