#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

engine = create_engine ("sqlite:///banco.db")
Base = declarative_base()

class Usuarios(Base):
    __tablename_ = 'usuarios'
    id = Column(Integer,primary_key=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)

if __name__ == '__main__':
    print engine
    Base.metadata.create_all(engine) 
    
