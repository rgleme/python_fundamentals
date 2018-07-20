#!/usr/bin/python

from Servidor import Servidor
from Acesso import Acesso

class Cloud(Servidor,Acesso):
	def __init__(self,disco=50,memoria=1024,cpu=1):
		self.url_acesso= "openstack.cloud.4linux.com.br/status"
		self.disco = disco
		self.cpu = cpu
		self.memoria = memoria

if __name__ == '__main__':
	cloud = Cloud()
	cloud.mostrarEnderecoIP()
	cloud.contratarDisco(10)
	cloud.contratarDisco(10)
	cloud.contratarDisco(10)
	cloud.mostrarConfiguracao()
	cloud.mostrarMetodoAcesso()
	cloud.statusMaquina()
	cloud.ligarMaquina()
