#!/usr/bin/python

from Usuarios.Usuarios import cadastro,acesso
import sys

def menu():
    while True:
        try:
            print " \
           1 - Cadastrar Usuario \n \
           2 - Acessar o Sistema \n \
           3 - Sair do Sistema"

            opcao = input ("Digite a opcao desejada: ")
            return opcao
        except Exception as e:
            print "Opcao Invalida: %s"%e
            return 3


def sair():
        sys.exit()

def switch(x):
    try:
        dict_options = {1:cadastro,2:acesso,3:sair}
        dict_options[x]()
    except Exception as e:
        print "Erro: %s"%e

if __name__ == '__main__':
    while True:
        switch(menu())
