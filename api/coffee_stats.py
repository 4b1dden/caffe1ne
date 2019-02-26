from flask_restful import Resource, Api
from flask import request
from mappings.CoffeeRequest import CoffeeRequest
from datetime import datetime, timedelta
import flask
import json

data = []

weekday_dict = {"Monday": "Pondelok", "Tuesday": "Utorok", "Wednesday": "Streda", "Thursday": "Štvrtok", "Friday": "Piatok", "Saturday": "Sobota", "Sunday": "Nedeľa"}

class CoffeeStats(Resource):
    def get(self):
        # stats_for = request.args.get("target")
        
        # stats for dashboard
        dashboard_stats = { "datasets": [] }
        labels = []

        start = datetime.now()
        week_delta = datetime.now() - timedelta(days=7)
        all_requests = flask.g.session\
                        .query(CoffeeRequest)\
                        .filter(CoffeeRequest.roastAt > week_delta)\
                        .order_by(CoffeeRequest.roastAt.asc())\
                        .all()
        
        while week_delta < start:
            week_delta = week_delta + timedelta(days=1)
            labels.append(weekday_dict[week_delta.strftime("%A")])

        dashboard_stats['labels'] = labels

        # how many coffees per day stat
        coffees_per_day = {
            "label": "Káv za deň",
        }

        week_data = []
        curr_day = datetime.now() - timedelta(days=6)

        while len(week_data) < 7:
            single_day = 0
            print("curr day is {}".format(curr_day.day))
            for req in all_requests:
                if req.roastAt.day == curr_day.day:
                    single_day += req.amount
            
            week_data.append(single_day)
            curr_day = curr_day + timedelta(days=1)

        coffees_per_day['data'] = week_data
        coffees_per_day['backgroundColor'] = ["#3e95cd"] * 7

        dashboard_stats['datasets'].append(coffees_per_day)

        return dashboard_stats
