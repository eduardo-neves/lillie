from sqlalchemy import Column, Integer, String, Float, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from . database.declarative import Base, Engine, Session
from . service_provider import Service_provider

class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    value = Column(Float)
    delivery = Column(Boolean)
    provider_id = Column(Integer, ForeignKey('service_providers.id'))

    def __repr__(self):
        return "<Service(name='%s', description='%s', value='%s', delivery='%s', provider_id=''%s)>" % (
            self.name, self.description, self.value, self.delivery, self.provider_id)
