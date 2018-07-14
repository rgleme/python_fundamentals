#!/usr/bin/python

import sys

lista = []
usuario = {"login":"","senha":""}

def cadastro():
    global lista
    usuario["login"]= raw_input ("Digite o login do usuario: ")
    usuario["senha"] = raw_input ("Digite a senha do usuario: ")
    lista.append(usuario)
    print "Usuario Cadastrado com Sucesso \n"

def acesso():
    global lista
    print "+Sistemas de Autenticacao"
    login = raw_input ("Digite o login do usuario: ")
    senha = raw_input ("Digite a senha do usuario: ")

    for u in lista:
        if u["login"] == login and u["senha"] == senha:
            print "Usuario autenticado com sucesso \n"
            break
        else:
            print "Falha ao autenticar \n"
    else:
        print "Usuario nao encontrado \n"

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
            print "Erro: %s"%e
            return 3


def sair():
        sys.exit()

def switch(x):
    try:
        dict_options = {1:cadastro,2:acesso,3:sair}
        dict_options[x]()
    except Exception as e:
        print "Opcao Invalida"

if __name__ == '__main__':
    while True:
        switch(menu())
