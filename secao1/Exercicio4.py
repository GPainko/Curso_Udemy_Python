"""
Exercicio

peça ao usuário para digitar seu nome
peça ao usuário para digitar seua idade
se nome e idade forem digitados:
    exiba:
        seu nome é {nome}
        seu nome invertido é{nome invertido}
        seu nome contém(ou não) espaço
        seu nome tem {n} letras
        a primeira letra do seu nome é {letras}
        a ultima letra do seu nome é {letras}
se nada for digitado em nome ou idade:
    exiba "Desculpa, você deixou campos vazios"
"""

nome = input("digite seu nome: ")
idade = input("digite sua idade: ")

if nome != '' and idade != '':#nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if ' ' in nome:
        print("seu nome tem espaço")
    else:
        print("seu nome não tem espaço")
    print(f'seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'a última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe,você deixou campos vazios.')    
