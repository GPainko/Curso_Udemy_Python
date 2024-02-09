#Métodos em instÃncia de classes Python
#Hard Coded - é algo que foi escrito diretamente no código
class Carro:
    def __init__(self,nome='Sem informação'):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...\n')

fusca = Carro('fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('celta')
print(celta.nome)
celta.acelerar()

veiculo = Carro()
print(veiculo.nome) 