from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)

from .meta import Base


class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    symbol = Column(String, nullable=False, unique=True)
    companyName = Column(String)
    CEO = Column(String)
    website = Column(String)
    industry = Column(String)
    sector = Column(String)
    exchange = Column(String)
    issueType = Column(String)
    description = Column(String)


Index('my_index', MyModel.name, unique=True, mysql_length=255)
