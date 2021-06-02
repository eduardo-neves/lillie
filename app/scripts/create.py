import sqlalchemy
from models.database.declarative import Base, Engine
from models import User

Base.metadata.create_all(Engine)
