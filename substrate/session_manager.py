import datetime
from enums import COFFEE_MACHINE_CONNECTION, COFFEE_REQUEST_STATUS
from contextlib import contextmanager
from coffee_request import CoffeeRequest
import sched, time


# coffee machine session manager class
class SessionManager:
    def __init__(self):
        print("SessionManager init")
        self.INIT_TIME_AT = datetime.datetime.now()
        self.SESSION_REQUESTS = []

    #handle connection to the coffee machine
    def connect(self):
        print("connecting to coffee machine...")
        self.COFFEE_MACHINE_CONNECTION_STATUS = COFFEE_MACHINE_CONNECTION.IS_CONNECTED
        return self.COFFEE_MACHINE_CONNECTION_STATUS

    #check whether session is connected
    def is_connected(self):
        return self.COFFEE_MACHINE_CONNECTION_STATUS == 1

    # coffee_request_model properties: name, amount, intensity, roastRightAway, roastAt
    def request_coffee(self, coffee_request_model):
        req = CoffeeRequest(coffee_request_model)
        
        self.addRequestToSessionRequests(req)
        #simulate actually requesting the machine to make the coffee
        if req.roastRightAway:
            req.make()
        else:
            req.setRequestStatus(COFFEE_REQUEST_STATUS.PENDING_REQUEST)
            # yield req.getRequestStatus()
            scheduler = sched.scheduler(time.time, time.sleep)
            # todo: change time to match user provided time from frontend
            scheduler.enter(5, 1, req.make)
            print('running the scheduler')
            scheduler.run()

        return req.getRequestStatus()
        
    def addRequestToSessionRequests(self, r):
        self.SESSION_REQUESTS.append(r)