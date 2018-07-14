#!/usr/bin/python

usuarios = []
senhas = []

while True:
    print "\
            1 - Cadastrar Usuario \n \
           2 - Acessar o Sistema \n \
           3 - Sair do Sistema"

    opcao = input ("Digite a opcao desejada: ")
    if opcao ==1:
        login = raw_input ("Digite o login do usuario: ")
        senha = raw_input ("Digite a senha do usuario: ")
        usuarios.append(login)
        senhas.append(senha)
        print "Usuario Cadastrado com Sucesso \n"

    elif opcao ==2:
        print "+Sistemas de Autenticacao"
        login = raw_input ("Digite o login do usuario: ")
        senha = raw_input ("Digite a senha do usuario: ")

        for i,u in enumerate(usuarios):
            if u == login:
                if senha == senhas[i]:
                    print "Usuario autenticado com sucesso \n"
                    break
                else:
                    print "Senha incorreta \n"
                    break
        else:
            print "Usuario nao encontrado \n"
            break
    elif opcao == 3:
        break
