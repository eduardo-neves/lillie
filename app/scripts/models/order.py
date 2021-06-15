from sqlalchemy import Column, Integer, String, Float, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from . database.declarative import Base, Engine, Session
from . service_provider import Service_provider
from . service import Service
from . user import User

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    provider_id = Column(Integer, ForeignKey('service_providers.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    status = Column(Integer, nullable=False)
