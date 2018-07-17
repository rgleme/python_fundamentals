#!/usr/bin/python

from Models.Model import session,Servidores

def cadastro_servidor():
    try:
        print "\n+Sistemas de Autenticacao\n"

        servidor = {}
        servidor["nome"]= raw_input ("Digite o nome do servidor: ")
        servidor["endereco"]= raw_input ("Digite o endereco IP do servidor: ")
        servidor["administrador"] = raw_input ("Digite o adm do servidor: ")
        srv = Servidores(servidor["nome"],servidor["endereco"],servidor["administrador"])
	session.add(srv)
        session.commit()
        print "\nServidor Cadastrado com sucesso\n"
    except Exception as e:
        print "Falhou ao inserir no banco %s"%e
        session.rollback()

def remover_servidor():
    try:
        srvs = session.query(Servidores).all()
        for s in srvs:
            print " %s - %s "%(s.id,s.nome)
        srv = input ("Digite o numero do servidor que deseja remover: ")
        srv_remove = session.query(Servidores).filter(Servidores.id==srv).first()
	session.delete(srv_remove)
        session.commit()
        print "\nServidor removido com sucesso\n"

    except Exception as e:
        print "Falhou ao remover do BD %s"%e

def definir_adm():
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
