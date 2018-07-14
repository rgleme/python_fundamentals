#!/usr/bin/python

import os
import json

def cadastro_usuario():
    usuarios = []
    if not os.stat("banco.json").st_size == 0:
        with open("banco.json","r") as f:
            dicionario_usuarios = json.load(f)
        usuarios = dicionario_usuarios["usuarios"]
        dicionario_usuarios["usuarios"] = usuarios
    else:
        dicionario_usuarios = {"usuarios":usuarios}

    usuario = {"login":"","senha":""}
    usuario["login"]= raw_input ("Digite o login do usuario: ")
    usuario["senha"] = raw_input ("Digite a senha do usuario: ")
    usuarios.append(usuario)
    try:
        with open("banco.json","w") as f:
            json.dump(dicionario_usuarios,f)
        print "Usuario Cadastrado com Sucesso \n"
    except Exception as e:
        print "Falhou ao escrever no arquivo %s"%e

def acesso():
    if not os.stat("banco.json").st_size == 0:
        with open("banco.json","r") as f:
            dicionario_usuarios = json.load(f)

    print "+Sistemas de Autenticacao"
    login = raw_input ("Digite o login do usuario: ")
    senha = raw_input ("Digite a senha do usuario: ")

    for u in dicionario_usuarios["usuarios"] :
        if u["login"] == login and u["senha"] == senha:
            print "Usuario autenticado com sucesso \n"
            break
    else:
        print "Falha de Autenticacao \n"
