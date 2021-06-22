from app.scripts.models import service_provider


def fetchProvider(provider_id):
    from . models.database.declarative import Base, Session, Engine
    from . models.service_provider import Service_provider

    session = Session()
    for provider in session.query(Service_provider).order_by(Service_provider.id).filter(Service_provider.id == provider_id):

        returnProvider = Service_provider(id=provider.id,
        name=provider.name, 
        document=provider.document, 
        email=provider.email,
        password=provider.password,
        phone=provider.phone, 
        address=provider.address, 
        address2=provider.address2, 
        cep=provider.cep,
        rating=provider.rating
        )
 
    return returnProvider

def loginProvider(provider_email):
    from . models.database.declarative import Base, Session, Engine
    from . models.service_provider import Service_provider

    session = Session()
    for provider in session.query(Service_provider).order_by(Service_provider.id).filter(Service_provider.email == provider_email):

        returnProvider = Service_provider(id=provider.id,
        name=provider.name, 
        document=provider.document, 
        email=provider.email,
        password=provider.password,
        phone=provider.phone, 
        address=provider.address, 
        address2=provider.address2, 
        cep=provider.cep,
        rating=provider.rating)
 
    return returnProvider

def listProvider():
    from . models.database.declarative import Base, Session, Engine
    from . models.service_provider import Service_provider

    session = Session()
    returnListProviders = []
    for provider in session.query(Service_provider).order_by(Service_provider.id):

        returnProvider = Service_provider(id=provider.id,
        name=provider.name, 
        document=provider.document, 
        email=provider.email,
        phone=provider.phone, 
        address=provider.address, 
        address2=provider.address2, 
        cep=provider.cep,
        rating=provider.rating)

        returnListProviders.append(returnProvider)  
    return returnListProviders
