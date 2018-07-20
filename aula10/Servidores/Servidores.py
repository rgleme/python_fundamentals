#!/usr/bin/python

from Models.Model import session,Servidores
from MongoDB.MongoFunctions import MongoFunctions
from Modulos.Docker import Docker
import json

class Servidores2:

	def __init__(self):
		pass
	def cadastro_servidor(self):
		try:
			print "\n+Sistemas de Autenticacao\n"

			servidor = {}
			servidor["nome"]= raw_input ("Digite o nome do servidor: ")
			servidor["administrador"] = raw_input ("Digite o adm do servidor: ")
			docker = Docker()
			docker.criarContainer(servidor['nome'])
			servidor["endereco"] = docker.pegarIPContainer(servidor["nome"])
			srv = Servidores(servidor["nome"],servidor["endereco"],servidor["administrador"])
			session.add(srv)
			session.commit()
			print "\nServidor Cadastrado com sucesso\n"
		except Exception as e:
			print "Falhou ao inserir no banco aqui %s"%e
			session.rollback()

	def remover_servidor(self):
	    try:
		srvs = session.query(Servidores).all()
		for s in srvs:
			print " %s - %s "%(s.id,s.nome)
		srv = raw_input ("Digite o nome do servidor que deseja remover: ")
		#docker = Docker()
		#docker.removerContainer(srv)
		srv_remove = session.query(Servidores).filter(Servidores.nome==srv).first()
		session.delete(srv_remove)
		session.commit()
		print "\nServidor removido com sucesso\n"

	    except Exception as e:
		print "Falhou ao remover do BD %s"%e

	def definir_adm(self):
	    try:        
		srvs = session.query(Servidores).all()
		for s in srvs:
		    print " %s - %s Administrador Atual [%s]"%(s.id,s.nome,s.administrador)
		srv = input ("Digite o numero do servidor que deseja definir o adm: ")
		admin = raw_input ("Digite o nome/email do administrador: ")
		srv_alterado = session.query(Servidores).filter(Servidores.id==srv).first()
		srv_alterado.administrador = admin
		session.commit()
		print "\nAdministrador atualizado comsucesso\n"

	    except Exception as e:
		print "Erro: %s"%e
		session.rollback()

	def acessar_servidor(self,login):

		try:        
			srvs = session.query(Servidores).all()
			for s in srvs:
			    print " %s - %s Administrador Atual [%s]"%(s.id,s.nome,s.administrador)
			srv = input ("Digite o numero do servidor que voce quer acessar: ")
			servidor = session.query(Servidores).filter(Servidores.id==srv).first()
			mf = MongoFunctions()			
			mf.registrar_logs(login,servidor.endereco_ip)

			docker = Docker()
			print "Para sair digite exit"
            		while True:
                		comando = raw_input("root@%s # "%servidor.nome)
                		print docker.acessarContainer(servidor.nome,comando)
                		if comando == "exit":
                    			break
		except Exception as e:
			print "Erro: %s"%e
			session.rollback()
