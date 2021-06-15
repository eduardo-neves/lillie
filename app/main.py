from flask import Flask, request, render_template, session, url_for, redirect
import app.scripts.models
import os
from dotenv import load_dotenv

load_dotenv()
  
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
  
@app.route("/")
def home_view():
        try:
                session['user_email'] != None
        except KeyError:
                return redirect(url_for('login'))
        else:
                from app.scripts.fetchProvider import fetchProvider
                providers = fetchProvider()
                loginString = "Sucessful login and authentication on " + session['user_email']
                return render_template('components/providerslist.html', providers=providers, loginString=loginString)
                
@app.route("/provider/<id>")
def provider(id):
        from app.scripts.fetchProvider import fetchProvider
        provider = fetchProvider()
        return render_template('components/providerslist.html', providers=provider)

@app.route("/services/<id>")
def service(id):
        from app.scripts.fetchService import fetchService
        services = fetchService(id)
        return render_template('components/serviceslist.html', services=services)


## http://127.0.0.1:5000/fetch/data
@app.route("/fetchuser/<id>")
def fetch(id):
        from app.scripts.fetchUser import fetchUser
        user = fetchUser(id)
        return render_template('register.html', user=user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
        if request.method == 'GET':
                return render_template('login.html')
        elif request.method == 'POST':
                from app.scripts.fetchUser import fetchUser
                user = fetchUser(request.form['user_email'])
                # print("Form password", request.form['user_password'])
                if user.verifyPassword(request.form['user_password']) == True:
                        session['user_id'] = user.id
                        session['user_email'] = user.email
                        return redirect(url_for('home_view'))
                else:
                        return str(user.verifyPassword(request.form['user_password']))
@app.route('/logout')
def logout():
        session.clear()
        return redirect(url_for('home_view'))

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404         


