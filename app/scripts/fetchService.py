def fetchService(provider_id):
    from . models.database.declarative import Base, Session, Engine
    from . models.service import Service

    session = Session()
    Services = []
    for service in session.query(Service).order_by(Service.id).filter(Service.provider_id == provider_id):
        
        returnService = Service(id=service.id,
        name=service.name, 
        description=service.description, 
        value=service.value,
        delivery=service.delivery, 
        provider_id=service.provider_id)

        Services.append(returnService)

    return Services