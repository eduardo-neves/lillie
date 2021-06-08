from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from . database.declarative import Base, Engine, Session

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    document = Column(String)
    email = Column(String)
    phone = Column(Integer)
    pj = Column(Boolean)
    adress = Column(String)
    adress2 = Column(String)
    cep = Column(Integer)

    orders = relationship('orders', backref='user')

    def __repr__(self):
        return "<User(name='%s', document='%s', email='%s', phone='%s', pj='%s', adress='%s', adress2='%s', cep='%s')>" % (
            self.name, self.document, self.email, self.phone, self.pj, self.adress, self.adress2, self.cep)
