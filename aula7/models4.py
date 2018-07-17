#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,Table
from sqlalchemy.orm import sessionmaker,relationship

engine = create_engine ("sqlite:///banco4.db")
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
Base = declarative_base()

class Token(Base):
	__tablename__ = 'token'
	id = Column(Integer,primary_key=True)
	analista_id = Column(Integer,ForeignKey("analistas.id"))
	servidores_id = Column(Integer,ForeignKey("servidores.id"))
	token = Column(String)
	servidor = relationship("Servidores")
	analista = relationship("Analistas")

class Analistas(Base):
	__tablename__ = 'analistas'
	id = Column(Integer,primary_key=True)
	nome = Column(String)
	servidor = relationship("Token")

	def __init__(self,id,nome):
		self.id = id
		self.nome = nome

class Servidores(Base):
	__tablename__ = 'servidores'
	id = Column(Integer,primary_key=True)
	endereco = Column(String)

	def __init__(self,id,endereco):
		self.id = id
		self.endereco = endereco
if __name__ == '__main__':
    try:
	pedro = session.query(Analistas).filter(Analistas.id==3).first()
	srv = session.query(Servidores).filter(Servidores.id==1).first()
	token = Token()
	token.id = 1
	token.token = "zcderf4545ffZC"
	session.add(token)
	pedro.servidores = token
	token.servidor = srv
	session.commit()
        Base.metadata.create_all(engine) 
    except Exception as e:
        print "Erro: %s"%e
     	session.rollback()
