from flask_restful import Resource, Api, reqparse
from mappings import CoffeeRequest
import flask
from datetime import datetime, timedelta

import os
import sys

#importing substrate
absFilePath = os.path.abspath(__file__)
fileDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(fileDir)
substrateDir = os.path.join(parentDir, "substrate")
print(substrateDir)

sys.path.append(substrateDir)

from session_manager import SessionManager

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('amount', type=int)
parser.add_argument('intensity', type=int)
parser.add_argument('roastRightAway', type=bool)
parser.add_argument('delayHours', type=int)
parser.add_argument('delayMinutes', type=int)

coffee_req_schema = CoffeeRequest.CoffeeRequest

_sm = SessionManager()

class Coffee(Resource):
    def get(self):
        return "Hello world"

    def post(request):
        args = parser.parse_args()
        roastAt = datetime.now()

        if not args.roastRightAway:
            roastAt = datetime.now() + timedelta(hours=args.delayHours, minutes=args.delayMinutes)

        req = coffee_req_schema(name=args.name, amount=args.amount, intensity=args.intensity, roastRightAway=args.roastRightAway, roastAt=roastAt)
        
        flask.g.session.add(req)
        # flask.g.session.commit()

        response_obj = args
        response_obj["willRoastAt"] = roastAt.strftime('%Y-%m-%dT%H:%M:%S')

        request_state = _sm.request_coffee(req)
        response_obj["requestState"] = {
            "enum": request_state.name,
            "code": request_state.value
        }

        return response_obj