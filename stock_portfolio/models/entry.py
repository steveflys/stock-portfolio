from sqlalchemy import(
    Column,
    Integer,
    String,
    DateTime,
)


from .meta import Base


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    Symbol = Column(String, nullable=False, unique=True)
    Company name = Column(String, nullable=False)
    CEO = Column(String, nullable=False)
    Website = Column(String, nullable=False)
    Industry = Column(String, nullable=False)
    Sector = Column(String, nullable=False)
    Exchange = Column(String, nullable=False)
    Issue Type = Column(String, nullable=False)
    Description = Column(String, nullable=False)

