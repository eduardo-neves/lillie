from flask import Flask
from app.scripts.dbDAO import testDb
  
app = Flask(__name__)
  
@app.route("/")
def home_view():
        return testDb()
