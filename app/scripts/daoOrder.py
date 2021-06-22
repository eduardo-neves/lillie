from sqlalchemy.sql.expression import select, insert
from sqlalchemy import desc
from datetime import datetime
from . models.database.declarative import Base, Session, Engine
from . models.order import Order
from . models.user import User
from . models.service_provider import Service_provider
from . models.service import Service

def createOrder(user_id, provider_id, service_id, delivery):
    if delivery == True:
        def_delivery = delivery
    else:
        def_delivery = False
    session = Session()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    stmt = insert(Order).values(user_id=user_id, provider_id=provider_id, service_id=service_id, status=1, placed_on=date, updated_on=date, delivery=def_delivery).returning(Order.id)

    for lines in session.execute(stmt).fetchall():
        for line in lines:
            orderId = line

    session.commit()

    return orderId


def fetchOrdersProvider(provider_id):

    orders = []
    session = Session()
    stmt = select(Order, Service, User).where(Order.provider_id==provider_id, Order.service_id==Service.id, Order.user_id==User.id).order_by(desc(Order.id))

    for result in session.execute(stmt):
        orders.append(result)

    return orders

def fetchOrdersUser(user_id):

    orders = []
    session = Session()
    stmt = select(Order, Service, Service_provider).where(Order.user_id==user_id, Order.service_id==Service.id, Order.provider_id==Service_provider.id).order_by(desc(Order.id))

    for result in session.execute(stmt):
        orders.append(result)

    # print(orders)
    return orders


def updateOrder(order_id, status):
    try:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        session = Session()
        for order in session.query(Order).order_by(Order.id).filter(Order.id == order_id):

            order.status = status
            order.updated_on = date

            session.add(order)
            session.commit()

            return True
    except:
        return False

