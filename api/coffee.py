from flask_restful import Resource, Api, reqparse
from mappings import CoffeeRequest
import flask
from datetime import datetime, timedelta

#importing substrate
# import sys
# import os
# lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../substrate'))
# sys.path.append(lib_path)


parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('amount', type=int)
parser.add_argument('intensity', type=int)
parser.add_argument('roastRightAway', type=bool)
parser.add_argument('delayHours', type=int)
parser.add_argument('delayMinutes', type=int)

coffee_req_schema = CoffeeRequest.CoffeeRequest

class Coffee(Resource):
    def get(self):
        return "Hello world"

    def post(request):
        args = parser.parse_args()
        roastAt = datetime.now()

        if not args.roastRightAway:
            roastAt = datetime.now() + timedelta(hours=args.delayHours, minutes=args.delayMinutes)

        req = coffee_req_schema(name=args.name, amount=args.amount, intensity=args.intensity, roastRightAway=args.roastRightAway, roastAt=roastAt)
        
        # todo: call substrate api
        flask.g.session.add(req)
        # flask.g.session.commit()

        response_obj = args
        response_obj["willRoastAt"] = roastAt.strftime('%Y-%m-%dT%H:%M:%S')

        # if args.roastRightAway:
        #     print("robim kavu....")
        #     resp = test.urobKavu()
        #     print("Mam response .. {}".format(resp))

        return response_obj