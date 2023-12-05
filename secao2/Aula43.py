#Ordem dos decoradores

def parametros_decorado(nome):
    def decorador(func):
        print('Decorador:',nome)

        def sua_nova_funcao(*args,**kwargs):
            res = func(*args,**kwargs)
            final = f'{res}, {nome}'
            return final
        return sua_nova_funcao
    return decorador


@parametros_decorado(nome='primeiro')
def soma(x,y):
    return x+y


@parametros_decorado(nome='segundo')
def subtracao(x,y):
    return x-y


dez_mais_cinco = soma(10,5)
dez_menos_cinco = subtracao(10,5)
print(dez_mais_cinco)
print(dez_menos_cinco)