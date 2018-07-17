#!/usr/bin/python

from Usuarios.Usuarios import cadastro_usuario,acesso,redefinir_senha
from Servidores.Servidores import cadastro_servidor,remover_servidor,definir_adm
from MongoDB.MongoFunctions import listar_ultimos_acessos
import sys

def menu():
    while True:
        try:
	    listar_ultimos_acessos()
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
        dict_options = {
                        1:cadastro_usuario,
                        2:acesso,
                        3:cadastro_servidor,
                        4:remover_servidor,
                        5:definir_adm,
                        6:redefinir_senha,
                        7:sair
                        }
        dict_options[x]()
    except Exception as e:
        print "Erro: %s"%e

if __name__ == '__main__':
    while True:
        switch(menu())
