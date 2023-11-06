import os

"""
Faça uma lista de comprar com lista
O usuário deve ter a possibilidade 
de inserir, apagar e listar valores
de sua lista.
Não permitir que o programa quebre 
com erros de indices inexistentes 
na lista
"""
lista_compras = []
while True:
    print('Escolha uma opção:')
    opcao = input('[a]adicionar [r]remover [l]listar: ')
    opcao = opcao.lower()

    if opcao == 'a':
        os.system('clear')
        produto = input('Qual produto deseja adicionar na lista: ')
        lista_compras.append(produto)
        
    elif opcao == 'r':
        os.system('clear')
        produto = input('Qual produto deseja remover da lista: ')
        for indice, nome in enumerate(lista_compras):
            if produto == nome:
                lista_compras.pop(indice)
                
    elif opcao == 'l':
        os.system('clear')
        print('sua lista de compras:')
        for produtos in lista_compras:
            print(produtos)
    else:
        os.system('clear')
        print('opção invalida')