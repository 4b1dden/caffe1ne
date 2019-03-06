from enums import COFFEE_REQUEST_STATUS

class CoffeeRequest:
    def __init__(self, req):
        self.name = req.name
        self.intensity = req.intensity
        self.amount = req.amount
        self.roastRightAway = req.roastRightAway
        self.roastAt = req.roastAt
    
    def setRequestStatus(self, s):
        self.requestStatus = s
        self.wasSuccessful = self.requestStatus == 1

    def getRequestStatus(self):
        return self.requestStatus

    def make(self):
        print("MAKING COFFEE FROM COFFEEREQUEST")
        self.setRequestStatus(COFFEE_REQUEST_STATUS.SUCCESSFUL)
        pass
        # actually comunicates with coffee machine
    