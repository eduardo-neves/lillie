def fetchProvider():
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

fetchProvider()