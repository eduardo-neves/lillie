from flask import Flask, request
from app.scripts.dbDAO import testDb
  
app = Flask(__name__)
  
@app.route("/")
def home_view():
        return testDb()


## http://127.0.0.1:5000/fetch/data
@app.route("/fetch/<data>")
def fetch(data):
        return data
        
## http://127.0.0.1:5000/fetch?data=data
@app.route("/fetch")
def fetchWithArgs():
        return request.args.get('data')
        
