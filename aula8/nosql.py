#!/usr/bin/python

from pymongo import MongoClient

try:
    client = MongoClient("127.0.0.1")
    db = client ["python"]
    print "Conexao OK"
    #db.exemplo.insert({"_id":1,"analista":"Steve Jobs","servidores":[]})
    db.exemplo.update({"_id":1,"servidores.nome":"nginx"},
                      {"$set":{"servidores.$.endereco":"192.168.0.97"}}
                     )
                             
    for d in db.exemplo.find({}):
	print d
            #print db.exemplo.find({})
    #for d in db.exemplo.find({}):
    #    print d["analista"]

except Exception as e:
    print "Erro: %s"%e
