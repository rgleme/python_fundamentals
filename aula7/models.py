#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

engine = create_engine ("sqlite:///banco.db")
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer,primary_key=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)

class Clientes(Base):
    __tablename__ = 'clientes'
    id = Column(Integer,primary_key=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)

class Funcionarios(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer,primary_key=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)

if __name__ == '__main__':
    try:
        #usuario = Usuarios()
        #usuario.id = 2
        #usuario.nome = "Jose do Egito"
        #print usuario.__dict__
        #session.add(usuario)

	#usuario = session.query(Usuarios).filter(Usuarios.id==2).first()
	#print usuario.nome
 
	#usuario = session.query(Usuarios).all()
	#for u in usuario:
	#	print u.id," - ",u.nome
	
	#usuario = session.query(Usuarios).filter(Usuarios.id==4).first()
	#session.delete(usuario)

	usuario = session.query(Usuarios).filter(Usuarios.id==2).first()
	usuario.nome = "Rodolfo Leme"       
        session.commit()
        #print "Usuario cadastrado com sucesso"
        Base.metadata.create_all(engine) 
    except Exception as e:
        print "Erro: %s"%e
     	session.rollback()
