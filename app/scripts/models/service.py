from sqlalchemy import Column, Integer, String, Float, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from . database.declarative import Base, Engine, Session
from . service_provider import Service_provider

class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text)
    value = Column(Float, nullable=False)
    delivery = Column(Boolean, nullable=False)
    provider_id = Column(Integer, ForeignKey('service_providers.id'), nullable=False)

    def __repr__(self):
        return "<Service(name='%s', description='%s', value='%s', delivery='%s', provider_id=''%s)>" % (
            self.name, self.description, self.value, self.delivery, self.provider_id)
