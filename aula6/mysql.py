#!/usr/bin/python

import MySQLdb

try:
    con =  MySQLdb.connect(host="127.0.0.1",user="devops",db="python",passwd="Htdrbps3")
    print "Conexao OK"
    cur = con.cursor()
    cur.execute("insert into script(nome,conteudo) values ('4linux.py','python_bla_bla')")
    print "Dados inseridos com sucesso"
    con.commit()

except Exception as e:
    print "Erro: %s"%e
    con.rollback()

finally:
    cur.close()
    con.close()
    print "Conexao finalizada com sucesso"
