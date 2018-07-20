#!/usr/bin/python

from Servidor import Servidor
from Acesso import Acesso

class Fisico(Servidor,Acesso):

	def __init__(self,disco=1024,cpu=4,memoria=4096):
		self.url_acesso = "200.100.50.25/acesso"
		self.metodo_acesso = "IPMI"
		self.disco = disco
		self.cpu = cpu
		self.memoria = memoria
		self.slots = 4
		self.slots_ocupados = 1

	def contratarDisco(self,disco):
		if self.slots_ocupados <= self.slots:
			if disco == 1024 or disco == 512:
				self.slots_ocupados +=1
				self.disco += disco
			else:
				print "Tamanho de Disco Invalido"		
		else:
			print "Todos Slots Ocupados"
		

if __name__ == '__main__':
	hm01 = Fisico()
	hm01.endereco_ip = "192.168.0.1"
	hm01.mostrarEnderecoIP()
	hm01.mostrarConfiguracao()
	hm01.contratarDisco(1024)
	hm01.contratarDisco(1024)
	hm01.contratarDisco(1024)
	hm01.contratarDisco(1024)
	hm01.contratarDisco(1024)
	hm01.mostrarConfiguracao()
	hm01.mostrarMetodoAcesso()
	hm01.statusMaquina()
	hm01.ligarMaquina()
