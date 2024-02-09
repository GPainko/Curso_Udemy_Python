#Entendendo self em classes Python
class Carro:
    def __init__(self,nome='Sem informação'):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...\n')

uno = Carro('uno')
uno.acelerar()
Carro.acelerar(uno)