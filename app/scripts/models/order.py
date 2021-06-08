from sqlalchemy import Column, Integer, String, Float, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from . database.declarative import Base, Engine, Session
from . service_provider import Service_provider
from . service import Service
from . user import User

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    provider_id = Column(Integer, ForeignKey('service_providers.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
