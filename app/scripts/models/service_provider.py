from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from . database.declarative import Base, Engine, Session

class Service_provider(Base):
    __tablename__ = 'service_providers'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    document = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=False)
    address2 = Column(String)
    cep = Column(String, nullable=False)
    rating = Column(Float, nullable=False)

    distance = Column(String)

    def __repr__(self):
        return "{Service_provider(id='%s', name='%s', document='%s', email='%s', phone='%s', address='%s', address2='%s', cep='%s', rating='%s')}" % (
            self.id, self.name, self.document, self.email, self.phone, self.address, self.address2, self.cep, self.rating)
