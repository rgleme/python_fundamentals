#!/usr/bin/python

import psycopg2

try:
    con = psycopg2.connect("host=127.0.0.1 dbname=python user=devops password=4linux")
    print "Conexao OK \n\n"
    cur = con.cursor()

    #cur.execute("insert into scripts(nome,conteudo) values ('postgres.py','python_bla_bla')")
    cur.execute("select * from scripts")

    print "Quantidade de registros: ",len(cur.fetchall())

    for r in cur.fetchall():
        print r[0],r[1]
    #print "Insercao OK"
    con.commit()

except Exception as e:
    print "Erro: %s"%e
    con.rollback()

finally:
    cur.close()
    con.close()
