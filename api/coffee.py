from flask_restful import Resource, Api
import json

with open("example.json") as f:
    data = json.load(f)

class Coffee(Resource):
    def get(self):
        return data