import flask
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_cors import CORS

from coffee import Coffee
from coffee_stats import CoffeeStats

from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///agrimonia.db')
app = Flask(__name__)
CORS(app)
api = Api(app)

Session = sessionmaker(bind=engine)

api.add_resource(Coffee, '/coffee')
api.add_resource(CoffeeStats, '/coffee_stats')

@app.before_request
def create_session():
    flask.g.session = Session()

if __name__ == '__main__':
    app.run(port='5000')