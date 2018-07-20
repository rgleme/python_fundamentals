#!/usr/bin/python

class Carro:
    cor = "Vermelho"
    modelo = "Sedan"
    lugares = 5
    vel_max = 200
    vel_atual = 0

    def acelerar(self,acel):
        if self.vel_atual < self.vel_max and acel <= self.vel_max:
            self.vel_atual += acel
            print "Velocidade Atual ",self.vel_atual
        else:
            print "Limite de Velocidade atingido"

    def frear(self,acel):
        if self.vel_atual > 0:
            self.vel_atual -= acel
            print "Velocidade Atual ",self.vel_atual
        else:
            print "Carro ja parado"


if __name__ == '__main__':
    corsa = Carro()
    #print corsa.modelo
    #print corsa.vel_atual
    corsa.acelerar(100)
    corsa.frear(100)
    corsa.frear(100)
    print corsa.vel_atual
