from datetime import date
from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from . database.declarative import Base, Engine, Session


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    provider_id = Column(Integer, ForeignKey('service_providers.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    delivery = Column(Boolean, nullable=False)
    placed_on = Column(DateTime, nullable=False)
    updated_on = Column(DateTime,nullable=False)
    status = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Order(id='%s', user_id='%s', provider_id='%s', service_id='%s', placed_on='%s', updated_on='%s', status='%s')>" % (
            self.id, self.user_id, self.provider_id, self.service_id, self.placed_on, self.updated_on, self.status)

