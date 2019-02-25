from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_cors import CORS

from coffee import Coffee

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(Coffee, '/coffee')

if __name__ == '__main__':
    app.run(port='5000')