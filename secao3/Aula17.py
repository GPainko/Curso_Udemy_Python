class Pessoa:
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.__class__.__name__)

class Cliente(Pessoa):
    ...


c1 = Cliente('Luiz','Otavio')
c1.falar_nome_classe()
