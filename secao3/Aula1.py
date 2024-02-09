# Class - classes são objetos para criar novos objetos 
# As classes geram novos objetos (instancias) que podem
# ter seus proprios atributos e metodos.
# Os objetos gerados pela classe podem usar seus dados 
# internos para realizar varias açoes

class Pessoa:
    def __init__(self, nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1=Pessoa('luiz','otavio')
print(p1.nome)
print(p1.sobrenome)