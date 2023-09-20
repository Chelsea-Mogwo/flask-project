from flask import Flask
from application import app
from application.aot_characters import routes
from application import routes

if __name__ == "__main__":
    app.run()