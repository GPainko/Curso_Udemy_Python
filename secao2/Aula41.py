#decoradores são "Syntax Sugar"(açúcar sintático)

def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            print('vou te decorar')
            e_string(arg)
        
        resultado = func(*args, **kwargs)
        resultado += ' QUAKL'
        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]


def e_string(param):
    if not isinstance(param,str):
        raise TypeError('param deve ser uma string')


invertida = inverte_string('123')
print(invertida)