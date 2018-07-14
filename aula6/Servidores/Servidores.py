#!/usr/bin/python

import psycopg2

def cadastro_servidor():
    try:
        print "\n+Sistemas de Autenticacao\n"

        con = psycopg2.connect("host=127.0.0.1 dbname=admssh user=dexter password=4linux")
        cur = con.cursor()
        servidor = {}
        servidor["nome"]= raw_input ("Digite o nome do servidor: ")
        servidor["endereco"]= raw_input ("Digite o endereco IP do servidor: ")
        servidor["administrador"] = raw_input ("Digite o adm do servidor: ")
        cur.execute ("insert into servidores (nome,endereco_ip,administrador) values ('%s','%s','%s')"%(servidor["nome"],servidor["endereco"],servidor["administrador"]))
        con.commit()
        print "\nServidor Cadastrado com sucesso\n"
    except Exception as e:
        print "Falhou ao inserir no banco %s"%e
        con.rollback()
    finally:
        cur.close()
        con.close()

def remover_servidor():
    try:
        con = psycopg2.connect("host=127.0.0.1 dbname=admssh user=dexter password=4linux")
        cur = con.cursor()
        cur.execute("select * from servidores")
        for s in cur.fetchall():
            print " %s - %s "%(s[0],s[1])
        srv = input ("Digite o numero do servidor que deseja remover: ")
        cur.execute("delete from servidores where id = %s"%srv)
        con.commit()
        print "\nServidor removido com sucesso\n"

    except Exception as e:
        print "Falhou ao remover do BD %s"%e

    finally:
        con.close()
        cur.close()

def definir_adm():
    try:
        con = psycopg2.connect("host=127.0.0.1 dbname=admssh user=dexter password=4linux")
        cur = con.cursor()
        cur.execute("select * from servidores")
        for s in cur.fetchall():
            print " %s - %s "%(s[0],s[1])
        srv = input ("Digite o numero do servidor que deseja definir o adm: ")
        admin = raw_input ("Digite o nome/email do administrador: ")
        cur.execute("update servidores set administrador = '%s' where id = '%s'"%(admin,srv))
        con.commit()
        print "\nAdministrador atualizado comsucesso\n"

    except Exception as e:
        print "Falhou ao remover do BD %s"%e
    
    finally:
        con.close()
        cur.close()
