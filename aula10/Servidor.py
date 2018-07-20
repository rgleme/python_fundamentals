#!/usr/bin/python

class Servidor:
	endereco_ip = "0.0.0.0"
	nome = "servidor"
	disco = 0
	memoria = 0
	cpu = 0

	def __init__(self):
		pass

	def mostrarEnderecoIP(self):
		print self.endereco_ip

	def contratarDisco(self,tamanho):
		self.disco += tamanho

	def contratarMemoria(self,mem):
		self.memoria += mem

	def contratarCPU(self,cpu):
		self.cpu += cpu

	def mostrarConfiguracao(self):
		print "Memoria Atual: ",self.memoria,"MB"
		print "CPU Atual: ",self.cpu
		print "Disco Atual: ",self.disco,"GB"
		
