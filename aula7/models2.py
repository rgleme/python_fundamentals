#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

engine = create_engine ("sqlite:///banco2.db")
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
Base = declarative_base()

class Funcionarios(Base):
	__tablename__ = 'funcionarios'
	id = Column(Integer,primary_key=True)
	nome = Column(String)
	dependentes = relationship("Dependentes")

class Dependentes(Base):
	__tablename__ = 'dependentes'
	id = Column(Integer,primary_key=True)
	nome = Column(String)
	funcionarios_id = Column(Integer,ForeignKey('funcionarios.id'))

if __name__ == '__main__':
    try:
	joao = session.query(Funcionarios).filter(Funcionarios.id==1).first()	
	joao = Funcionarios ()
	marcelo = Dependentes()
	marcelo.id = 2
	marcelo.nome = "Marcelo"
	session.add(marcelo)
	joao.dependentes.append(marcelo)
	joao.id = 1
	joao.nome = "Joao"
	session.add(joao)
	maria = Dependentes()
	maria.id = 1
	maria.nome = "Maria"
	session.add(maria)
	joao.dependentes.append(maria)
	session.commit()
        Base.metadata.create_all(engine) 
    except Exception as e:
        print "Erro: %s"%e
     	session.rollback()
