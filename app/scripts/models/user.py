from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from passlib.hash import sha256_crypt
from . database.declarative import Base, Engine, Session

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    document = Column(String)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    pj = Column(Boolean)
    address = Column(String, nullable=False)
    address2 = Column(String)
    cep = Column(Integer, nullable=False)

    def __repr__(self):
        return "<User(name='%s', document='%s', email='%s', phone='%s', pj='%s', address='%s', address2='%s', cep='%s')>" % (
            self.name, self.document, self.email, self.phone, self.pj, self.address, self.address2, self.cep)

    def encryptPassword(self, password):
        self.password = sha256_crypt.hash(password)
            
    def verifyPassword(self, password):
        if sha256_crypt.verify(password, self.password) == True:
            print("Returned True")
            return True
        else:
            return False
