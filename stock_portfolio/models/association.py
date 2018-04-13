from sqlalchemy import (
    Column,
    Integer,
    Table,
    ForeignKey,
)
from .meta import Base


association_table = Table(
    'association', Base.metadata,
    Column('account_id', Integer, ForeignKey('accounts.id')),
    Column('stock_id', Integer, ForeignKey('stock.id'))
)
