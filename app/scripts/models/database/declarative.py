import os
from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
Engine = create_engine(os.getenv('DATABASE_URL'), echo=True)
Session = sessionmaker(bind=Engine)
Base = declarative_base()

# try:
#     conn = Engine.connect()
#     conn.close()
#     print("Success")
# except:
#     print("Failed")