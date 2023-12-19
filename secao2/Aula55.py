#problema dos parametros mutaveis em funções python

def adiciona_clientes(nome,lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('luiz')
adiciona_clientes('joana',cliente1)
adiciona_clientes('fernando',cliente1)
cliente1.append('edu')
print(cliente1)

cliente2 = adiciona_clientes('maria')
adiciona_clientes('joao',cliente2)
print(cliente2)