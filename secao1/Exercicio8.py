"""
Iterando strings com while
"""

nome = "Guilherme Painko Scalcon"

tamanho_nome = len(nome)

contador = 0

while contador < tamanho_nome:
    print(nome[contador] + ' ' +nome[contador - 1])
    nova_string = (f'{nome[contador]}' + ' - ' * 5)
    print(nova_string)
    contador += 1