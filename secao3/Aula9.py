# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja
# ao invés de receber a instância no primeiro 
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2024 #atributo de classe

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls,nome):
        return cls(nome,50)

    @classmethod
    def sem_nome(cls,idade):
        return cls('Anônima',idade)


p1 = Pessoa('João',43)
p2 = Pessoa.criar_com_50_anos('José')
p3 = Pessoa.sem_nome(20)
Pessoa.metodo_de_classe()
print(p2.nome,p2.idade)
print(p3.nome,p3.idade)