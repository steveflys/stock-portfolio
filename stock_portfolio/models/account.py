from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)

from .meta import Base


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer)
    password = Column(String, nullable=False, unique=True)
    email = Column(String)
    username = Column(String)

# Index('my_index', MyModel.name, unique=True, mysql_length=255)
