from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.json_provider_class.sort_keys = False # orders the data
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://wymctuwy:zFfCnWUQJg43dofVfBVhAbAr77h3NSNk@tai.db.elephantsql.com/wymctuwy"

db = SQLAlchemy(app)