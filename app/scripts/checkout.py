from . models.database.declarative import Base, Session, Engine
from . models.service import Service
from . models.service_provider import Service_provider

def checkout(service_id):
    
    session = Session()
    data = []
    for service, provider in session.query(Service, Service_provider).\
        filter(Service.id==service_id).\
        filter(Service.provider_id==Service_provider.id).\
        all():

        returnService = Service(
            id=service.id,
            name=service.name,
            description=service.description,
            value=service.value,
            delivery=service.delivery
            )
        
        data.append(returnService)

        returnProvider = Service_provider(
            id=provider.id,
            name=provider.name, 
            email=provider.email,
            phone=provider.phone, 
            address=provider.address, 
            address2=provider.address2, 
            cep=provider.cep,
            rating=provider.rating
            )

        data.append(returnProvider)

    return data
