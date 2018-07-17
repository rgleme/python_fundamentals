#!/usr/bin/python

from Models.Model import session,Usuarios
from Servidores.Servidores import acessar_servidor

def cadastro_usuario():
    try:

        usuario = {}
        usuario["nome"]= raw_input ("Digite o nome do usuario: ")
        usuario["email"]= raw_input ("Digite o email do usuario: ")
        usuario["senha"] = raw_input ("Digite a senha do usuario: ")

	us = Usuarios(usuario["nome"],usuario["email"],usuario["senha"])
	session.add(us)
	session.commit()
        print "\nUsuario cadastrado com sucesso\n"
    except Exception as e:
        print "Falhou ao inserir no banco %s"%e
        session.rollback()

def acesso():
    try:
        print "+Sistemas de Autenticacao\n"
        email = raw_input ("Digite o email do usuario: ")
        senha = raw_input ("Digite a senha do usuario: ")
        res = session.query(Usuarios).filter(Usuarios.email==email,Usuarios.senha==senha).first()
        if res is None:
            print "\nAcesso Negado\n"
        else:
            print "\nUsuario autenticado\n"
	    acessar_servidor(res.email)
    except Exception as e:
            print "Falha ao consultar no banco %s"%e
            session.rollback()

def redefinir_senha():
    try:
        email = raw_input ("Digite o email do usuario: ")
        senha = raw_input ("Digite a senha do usuario: ")
	res = session.query(Usuarios).filter(Usuarios.email==email,Usuarios.senha==senha).first()
        if res is None:
            print "\nUsuario ou senha invalidos\n"
        else:
            nova_senha = raw_input ("Digite a nova senha: ")
            res.senha = nova_senha
            session.commit()
            print "\n Senha atualizada com sucesso\n"
    except Exception as e:
        print "Falha ao consultar no banco %s"%e
        session.rollback()
