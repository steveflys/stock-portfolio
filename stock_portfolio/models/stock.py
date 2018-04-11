from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
    ForeignKey,
)

from .meta import Base


class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    account_id = Column(Text, ForeignKey('accounts.username', nullable=False))
    symbol = Column(String, nullable=False, unique=True)
    companyName = Column(String)
    CEO = Column(String)
    website = Column(String)
    industry = Column(String)
    sector = Column(String)
    exchange = Column(String)
    issueType = Column(String)
    description = Column(String)


# Index('my_index', Stock.symbol, unique=True, mysql_length=255)
