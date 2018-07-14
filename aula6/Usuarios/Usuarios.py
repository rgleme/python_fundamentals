#!/usr/bin/python

import psycopg2

def cadastro_usuario():
    try:
        con = psycopg2.connect("host=127.0.0.1 dbname=admssh user=dexter password=4linux")
        cur = con.cursor()

        usuario = {}
        usuario["nome"]= raw_input ("Digite o nome do usuario: ")
        usuario["email"]= raw_input ("Digite o email do usuario: ")
        usuario["senha"] = raw_input ("Digite a senha do usuario: ")

        cur.execute("insert into usuarios (nome,email,senha) \
                     values ('%s','%s','%s')"%(
                                                usuario["nome"],
                                                usuario["email"],
                                                usuario["senha"]
                                              )
                   )
        con.commit()
        print "\nUsuario cadastrado com sucesso\n"
    except Exception as e:
        print "Falhou ao inserir no banco %s"%e
        con.rollback()
    finally:
        cur.close()
        con.close()

def acesso():
    try:
        print "+Sistemas de Autenticacao\n"
        con = psycopg2.connect("host=127.0.0.1 dbname=admssh user=dexter password=4linux")
        cur = con.cursor()
        email = raw_input ("Digite o email do usuario: ")
        senha = raw_input ("Digite a senha do usuario: ")
        cur.execute ("select * from usuarios where email = '%s' and senha = '%s'"%(email,senha))
        if cur.fetchone() is None:
            print "Acesso Negado"
        else:
            print "\nUsuario autenticado\n"
    except Exception as e:
            print "Falha ao consultar no banco %s"%e
            con.rollback()
    finally:
        cur.close()
        con.close()

def redefinir_senha():
    try:
        con = psycopg2.connect("host=127.0.0.1 dbname=admssh user=dexter password=4linux")
        cur = con.cursor()
        email = raw_input ("Digite o email do usuario: ")
        senha = raw_input ("Digite a senha do usuario: ")
        cur.execute ("select * from usuarios where email = '%s' and senha = '%s'"%(email,senha))
        if cur.fetchone() is None:
            print "\nUsuario ou senha invalidos\n"
        else:
            nova_senha = raw_input ("Digite a nova senha: ")
            cur.execute("update usuarios set senha = '%s' where email = '%s'"%(nova_senha,email))
            con.commit()
            print "\n Senha atualizada com sucesso\n"
    except Exception as e:
        print "Falha ao consultar no banco %s"%e
        con.rollback()
    finally:
        cur.close()
        con.close()
