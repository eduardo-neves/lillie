import sqlalchemy
from models.database.declarative import Base, Engine
from models.user import User
from models.service_provider import Service_provider
from models.service import Service
from models.order import Order

Base.metadata.create_all(Engine)
