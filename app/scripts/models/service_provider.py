from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . database.declarative import Base, Engine, Session

class Service_provider(Base):
    __tablename__ = 'service_providers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    document = Column(String)
    email = Column(String)
    phone = Column(Integer)
    address = Column(String)
    address2 = Column(String)
    cep = Column(Integer)

    services = relationship('services', backref='service_provider')

    def __repr__(self):
        return "<Service_provider(name='%s', document='%s', email='%s', phone='%s', address='%s', address2='%s', cep='%s')>" % (
            self.name, self.document, self.email, self.phone, self.address, self.address2, self.cep)
