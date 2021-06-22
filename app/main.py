## IMPORTS DEPENDENCIES
from flask import Flask, request, render_template, session, sessions, url_for, redirect, flash
import os
from dotenv import load_dotenv

## START DOTENV 
load_dotenv()

status_text = ["Cancelado por usuário", "Aguardando confirmação", "Cancelado por provedor", "Confirmado", "Em transito (coleta)", "Em transito (entrega)", "Em andamento", "Concluído"]

## APP STAGING
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER')


## BEGIN USER ROUTES AND FUNCTION USAGE
@app.route("/")
def index():
       return render_template('index.html')

@app.route("/user")
def homeView():
        try:
                session['user_id'] != None
        except KeyError:
                return redirect(url_for('loginUser'))
        else:
                from app.scripts.daoProvider import listProvider
                from app.scripts.functions.distance import distance
                providers = listProvider()
                for provider in providers:
                        distancia = distance(session['user_cep'], provider.cep)
                        provider.distance = distancia
                        starRounded = int(provider.rating)
                return render_template('components/providersList.html', providers=providers, starRounded=starRounded)

            
@app.route("/user/provider/<id>")
def provider(id):

        try:
                session['user_id'] != None
        except KeyError:
                return redirect(url_for('loginUser'))
        else:        
                from app.scripts.daoProvider import fetchProvider
                provider = fetchProvider()
                return render_template('components/providersList.html', providers=provider)

@app.route("/user/services/<id>")
def service(id):

        try:
                session['user_id'] != None
        except KeyError:
                return redirect(url_for('loginUser'))
        else:
                from app.scripts.daoService import fetchService
                from app.scripts.daoProvider import fetchProvider
                from app.scripts.functions.distance import distance
                services = fetchService(id)
                provider = fetchProvider(id)
                distancia = distance(session['user_cep'], provider.cep)
                provider.distance = distancia
                starRounded = int(provider.rating)
                return render_template('components/servicesList.html', services=services, provider=provider, starRounded=starRounded)


@app.route("/user/orders/")
def orders():

        try:
                session['user_id'] != None
        except KeyError:
                return redirect(url_for('loginUser'))
        else:
                from app.scripts.daoOrder import fetchOrdersUser
                order_data = fetchOrdersUser(session['user_id'])
                return render_template('components/listOrderUser.html', order_data=order_data, status_text=status_text)

@app.route("/user/updateorder", methods = ['POST'])
def updateOrder():
        if request.method != "POST":
                return redirect(url_for("orders"))
        else:
                from app.scripts.daoOrder import updateOrder
                if updateOrder(request.form['order_id'], 0):
                        flash("Pedido cancelado com sucesso.")
                        return redirect(url_for("orders"))
                else:
                        flash('Erro ao solicitar cancelamento. Tente novamente em breve')
                        return redirect(url_for("orders"))

@app.route("/user/profile")
def profile():
        return render_template('components/profileUser.html', test="This is where the profile is going to be.") 

@app.route("/user/checkout/<id>")
def checkout(id):

        try:
                session['user_id'] != None
        except KeyError:
                return redirect(url_for('login'))
        else:
                from app.scripts.checkout import checkout
                from app.scripts.functions.distance import distance
                checkout_data = checkout(id)
                service = checkout_data[0]
                provider = checkout_data[1]
                distancia = distance(session['user_cep'], provider.cep)
                provider.distance = distancia
                starRounded = int(provider.rating)
                return render_template('components/checkout.html', service=service, provider=provider, starRounded=starRounded)

@app.route('/user/checkout/processing', methods = ['POST'])
def checkout_processing():
        try:
                request.form != None
                print(request.form)
        except:
                return redirect(url_for('homeView'))
        else:
                from app.scripts.daoOrder import createOrder
                orderId = createOrder(session['user_id'], request.form['provider_id'], request.form['service_id'], request.form['delivery'])

                return render_template('components/checkoutSuccess.html', orderId=orderId)

@app.route('/user/login', methods = ['GET', 'POST'])
def loginUser():
        if request.method == 'GET':
                return render_template('components/login.html')
        elif request.method == 'POST':
                try:
                        from app.scripts.daoUser import fetchUser
                        user = fetchUser(request.form['user_email'])
                        if user.verifyPassword(request.form['user_password']) == True:
                                session['user_id'] = user.id
                                session['user_email'] = user.email
                                session['user_name'] = user.name
                                session['user_cep'] = user.cep
                                return redirect(url_for('homeView'))
                        else:
                                flash('Credenciais incorretas')
                                return redirect(url_for('loginUser'))
                except:
                        flash('E-mail não cadastrado')
                        return redirect(url_for('loginUser'))

@app.route('/logout')
def logout():
        if session['user_id']:
                session.clear()
                return redirect(url_for('homeView'))
        elif session['provider']:
                session.clear()
                return redirect(url_for('homeViewProvider'))

## END USER ROUTES
##
## BEGIN PROVIDER ROUTES AND FUNCTION USAGE
@app.route('/provider/login', methods = ['GET', 'POST'])
def loginProvider():
        if request.method == 'GET':
                return render_template('components/loginProvider.html')
        elif request.method == 'POST':
                try:
                        from app.scripts.daoProvider import loginProvider
                        provider = loginProvider(request.form['user_email'])
                        if provider.verifyPassword(request.form['user_password']) == True:
                                session['provider_id'] = provider.id
                                session['provider_email'] = provider.email
                                session['provider_name'] = provider.name
                                session['provider_cep'] = provider.cep
                                return redirect(url_for('homeViewProvider'))
                        else:
                                flash('Credenciais incorretas')
                                return redirect(url_for('loginProvider'))
                except:
                        flash('E-mail não cadastrado')
                        return redirect(url_for('loginProvider'))

@app.route("/provider")
def homeViewProvider():
        try:
                session['provider_id'] != None
        except KeyError:
                return redirect(url_for('loginProvider'))
        else:
                return redirect(url_for('ordersProvider'))

@app.route("/provider/orders")
def ordersProvider():

        try:
                session['provider_email'] != None
        except KeyError:
                return redirect(url_for('loginProvider'))
        else:
                from app.scripts.daoOrder import fetchOrdersProvider
                order_data = fetchOrdersProvider(session['provider_id'])
                return render_template('components/listOrderProvider.html', order_data=order_data, status_text=status_text)

@app.route("/provider/updateorder", methods = ['POST'])
def updateOrderProvider():
        if request.method != "POST":
                return redirect(url_for("ordersProvider"))
        else:
                from app.scripts.daoOrder import updateOrder
                if updateOrder(request.form['order_id'], request.form['status']):
                        flash("Pedido atual com sucesso.")
                        return redirect(url_for("ordersProvider"))
                else:
                        flash('Erro ao atualizar pedido. Tente novamente em breve')
                        return redirect(url_for("ordersProvider"))

## END PROVIDER ROUTES
##
## BEGIN UTILS AND ERROR HANDLING

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('components/404.html'), 404

@app.route("/demo")
def demo():
        session['user_email'] = "example@example.com" 
        session['user_id'] = 1
        session['user_cep'] = "88056300"
        return redirect(url_for("homeView"))
