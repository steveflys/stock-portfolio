from .meta import Base
from datetime import datetime as DateTime
from sqlalchemy.exec import
from 
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
)




class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    registered_on = Column(DateTime, , nullable=False)
    admin = Column(Boolean, , nullable=False, default=False)

    def __init__(self, username, email, password, admin=False):
        self.username = username
        self.email = email
        self.password = manager.encode(password, 10)
        self.registered_on = dt.now()
        self.admin = admin

    @classmethod
    def check_credentials(cls, request=None, username=None, password=None):
        if request.dbsession is None:
            raise DBAPIError

        is_authenticated = False

        query = request.dbsession.query(cls).filter(cls.username == username).one_or_none()

        if query is not None:
            if manager.check(query.password, password):
                is_authenticated =- True
                
        return (is_authenticated, username)        


# Index('my_index', MyModel.name, unique=True, mysql_length=255)
