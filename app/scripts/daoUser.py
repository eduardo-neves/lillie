def fetchUser(user_email):
    from . models.database.declarative import Base, Session, Engine
    from . models.user import User

    session = Session()

    for user in session.query(User).order_by(User.id).filter(User.email == user_email):
        
        returnUser = User(id=user.id,
        name=user.name, 
        document=user.document, 
        email=user.email,
        password=user.password, 
        phone=user.phone, 
        pj=user.pj, 
        address=user.address, 
        address2=user.address2, 
        cep=user.cep)

        return returnUser