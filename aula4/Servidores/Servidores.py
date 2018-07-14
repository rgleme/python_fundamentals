#!/usr/bin/python

import os
import json

def cadastro_servidor():
    servidores = []
    if not os.stat("servidores.json").st_size == 0:
        with open("servidores.json","r") as f:
            dicionario_servidores = json.load(f)
        servidores = dicionario_servidores["servidores"]
        dicionario_servidores["servidores"] = servidores
    else:
        dicionario_servidores = {"servidores":servidores}

    servidor = {"endereco":"","nome":"","administrador":""}
    servidor["endereco"]= raw_input ("Digite o endereco do Servidor: ")
    servidor["nome"] = raw_input ("Digite o nome do Servidor: ")
    servidor["administrador"] = raw_input ("Digite o ADM do Servidor: ")
    servidores.append(servidor)
    try:
        with open("servidores.json","w") as f:
            json.dump(dicionario_servidores,f)
        print "Servidor Cadastrado com Sucesso \n"
    except Exception as e:
        print "Falhou ao escrever no arquivo %s"%e

def remover_servidor():
    servidores = []
    if not os.stat("servidores.json").st_size == 0:
        with open("servidores.json","r") as f:
            dicionario_servidores = json.load(f)
        servidores = dicionario_servidores["servidores"]
        dicionario_servidores["servidores"] = servidores
    else:
        dicionario_servidores = {"servidores":servidores}
    print servidores
    for i,s in enumerate(servidores):
        print "%s - %s"%(i,s)
    srv = input ("Digite o numero do servidor que vc deseja remover: ")
    del dicionario_servidores["servidores"][srv]
    
    try:
        with open("servidores.json","w") as f:
            json.dump(dicionario_servidores,f)
        print "Servidor Removido com Sucesso \n"
    except Exception as e:
        print "Falhou ao escrever no arquivo %s"%e

def definir_adm():
    pass
