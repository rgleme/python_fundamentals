#!/usr/bin/python

from Usuarios.Usuarios import Usuarios2
from Servidores.Servidores import Servidores2
from MongoDB.MongoFunctions import MongoFunctions
import sys

def menu():
    while True:
        try:
	    mf = MongoFunctions()
	    mf.listar_ultimos_acessos()
            print " \n\
            1 - Cadastrar Usuario \n \
           2 - Acessar o Sistema \n \
           3 - Cadastrar Servidor \n \
           4 - Remover Servidor \n \
           5 - Definir Administrador \n \
           6 - Redefinir Senha \n \
           7 - Sair"

            opcao = input ("\nDigite a opcao desejada: ")
            return opcao
        except Exception as e:
            print "Opcao Invalida: %s"%e

def sair():
        sys.exit()

def switch(x):
    try:
	srv = Servidores2()
        usr = Usuarios2()
        dict_options = {
                        1:usr.cadastro_usuario,
                        2:usr.acesso,
                        3:srv.cadastro_servidor,
                        4:srv.remover_servidor,
                        5:srv.definir_adm,
                        6:usr.redefinir_senha,
                        7:sair
                        }
        dict_options[x]()
    except Exception as e:
        print "Erro: %s"%e

if __name__ == '__main__':
    while True:
        switch(menu())
