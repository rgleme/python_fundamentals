#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,Table
from sqlalchemy.orm import sessionmaker,relationship

engine = create_engine ("sqlite:///banco3.db")
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
Base = declarative_base()


analista_servidores = Table('analista_servidores',
	Base.metadata,
	Column('analistas_id',Integer,ForeignKey("analistas.id")),
	Column('servidores_id',Integer,ForeignKey("servidores.id"))
)

class Analistas(Base):
	__tablename__ = 'analistas'
	id = Column(Integer,primary_key=True)
	nome = Column(String)
	servidores = relationship("Servidores",secondary=analista_servidores)

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
	rodolfo = session.query(Analistas).filter(Analistas.id==1).first()
	srv1 = session.query(Servidores).filter(Servidores.id==3).first()
	srv2 = session.query(Servidores).filter(Servidores.id==4).first()
	rodolfo.servidores.append(srv1)
	rodolfo.servidores.append(srv2)
	#analista = Analistas(1,'rodolfo')
	#analista1 = Analistas(2,'jose')
	#analista2 = Analistas(3,'pedro')
	#analista3 = Analistas(4,'marcos')
	#session.add(analista)
	#session.add(analista1)
	#session.add(analista2)
	#session.add(analista3)

	#servidor = Servidores (1,'192.168.0.1')
	#servidor1 = Servidores (2,'192.168.0.2')
	#servidor2 = Servidores (3,'192.168.0.3')
	#servidor3 = Servidores (4,'192.168.0.4')
	#session.add(servidor)
	#session.add(servidor1)
	#session.add(servidor2)
	#session.add(servidor3)

	session.commit()
        Base.metadata.create_all(engine) 
    except Exception as e:
        print "Erro: %s"%e
     	session.rollback()
