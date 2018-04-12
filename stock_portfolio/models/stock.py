from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from .meta import Base
from .association import association_table


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
    account_id = relationship(
        'Account',
        secondary=association_table,
        back_populates="stock_id")
