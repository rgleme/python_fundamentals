#!/usr/bin/python

from Usuarios.Usuarios import cadastro_usuario,acesso
from Servidores.Servidores import cadastro_servidor,remover_servidor,definir_adm
import sys

def menu():
    while True:
        try:
            print " \
           1 - Cadastrar Usuario \n \
           2 - Acessar o Sistema \n \
           3 - Cadastrar Servidor \n \
           4 - Remover Servidor \n \
           5 - Definir Administrador \n \
           6 - Sair"

            opcao = input ("Digite a opcao desejada: ")
            return opcao
        except Exception as e:
            print "Opcao Invalida: %s"%e
            return 3


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
                        6:sair
                        }
        dict_options[x]()
    except Exception as e:
        print "Erro: %s"%e

if __name__ == '__main__':
    while True:
        switch(menu())
