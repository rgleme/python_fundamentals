#!/usr/bin/python

class Acesso:
	metodo_acesso = "SSH"
	status = "desligado"
	url_acesso = ""
	def __init__(self):
		pass

	def mostrarMetodoAcesso(self):
		print self.metodo_acesso

	def statusMaquina(self):
		print self.status
	
	def ligarMaquina(self):
		print "Acessando URL: ",self.url_acesso,"\n"
		self.status = "ligado"
		print "Maquina Ligada"
	
