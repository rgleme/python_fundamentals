#!/usr/bin/python

lista = []
usuario = {"login":"","senha":""}

while True:
    print "\
            1 - Cadastrar Usuario \n \
           2 - Acessar o Sistema \n \
           3 - Sair do Sistema"

    opcao = input ("Digite a opcao desejada: ")
    if opcao ==1:
        usuario["login"]= raw_input ("Digite o login do usuario: ")
        usuario["senha"] = raw_input ("Digite a senha do usuario: ")
        lista.append(usuario)
        print "Usuario Cadastrado com Sucesso \n"

    elif opcao ==2:
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
            break
    elif opcao == 3:
        break
