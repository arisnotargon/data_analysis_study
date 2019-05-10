from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import sqlalchemy as sqla
import sqlalchemy.orm

Base = declarative_base()

class Test(Base):
    __tablename__ = 'test'
    id = sqla.Column('id', sqla.Integer, primary_key=True)
    name = sqla.Column('name', sqla.String)
    query_at = sqla.Column('query_at', sqla.TIMESTAMP)
    created_at = sqla.Column("created_at", sqla.TIMESTAMP)
