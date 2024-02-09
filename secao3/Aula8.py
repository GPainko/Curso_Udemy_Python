#__dict__ e vars para atributos de instancia
class Pessoa:
    ano_atual = 2024

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
    
p1 = Pessoa('Carlos', 34)

p1.__dict__['outra'] = 'coisa'

print(p1.__dict__)

del p1.__dict__['outra']

print(vars(p1))

