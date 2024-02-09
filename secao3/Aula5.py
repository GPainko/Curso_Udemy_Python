# EScopo da classe e de metodos da classe

class Animal:

    #nome = 'Leão'
    def __init__(self,nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self,alimento = 'nada'):
        return f'{self.nome} está comendo {alimento}\n'
    
    def executar(self,*args, **kwargs):
        return self.comendo(*args,**kwargs)

leao = Animal('leão')
print(leao.nome)
print(leao.comendo('carne'))
print(leao.executar('carnes'))