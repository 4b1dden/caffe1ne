from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CoffeeRequest(Base):
    __tablename__ = "coffee_requests"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    intensity = Column(Integer)
    amount = Column(Integer)
    roastRightAway = Column(Boolean)
    roastAt = Column(DateTime)

    # def __repr__(self):
    #     return "<CoffeeRequest(by='%s', amount='%s', make_at='%s')>" % (
    #                             self.name, self.amount, self.roastAt)