from models.database.declarative import Base, Session, Engine
from models.user import User
from models.service_provider import Service_provider
from models.service import Service

def createUser():
    
    try:
        session = Session() 
        user = User(name='Test user name', document='99999999', email='example@example.com', password='$5$rounds=535000$MRiEAxe.Uzaxrv/X$Rd9qoPKfz58vVL1YHHzUr8kTfcAbPst4NGOkbC89.R2', phone='99999999', pj=False, address='Rua do teste 100', address2='Loja 1', cep='89300200')
        session.add(user)
        session.commit()
        return "Success"
    except:
        return "Failed"

def createProvider():
    
    try:
        session = Session() 
        provider = Service_provider(name='Test provider name', document='99999999', email='example_provider@example.com', password='$5$rounds=535000$MRiEAxe.Uzaxrv/X$Rd9qoPKfz58vVL1YHHzUr8kTfcAbPst4NGOkbC89.R2', phone='99999999', address='Rua do teste 100', address2='Loja 1', cep='89300200', rating='4.5')
        session.add(provider)
        session.commit()
        return "Success"
    except:
        return "Failed"

def createService():
    
    try:
        session = Session() 
        service = Service(name='Test service name 2', description='This is a test description', value=67.90, delivery=False, provider_id='1')
        session.add(service)
        session.commit()
        return "Success"
    except:
        return "Failed"

createService()