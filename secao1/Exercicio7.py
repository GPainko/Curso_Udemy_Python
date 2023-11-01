"""
Faça um programa que peça o primeiro nome do usuario, 
se o nome tiver 4 letras ou menos escreva "seu nome é curto"
se tiver entre 5 e 6 letras escreva "seu nome é normal"
se tiver mais de 6 letras escreva "seu nome é muit grande"
"""

primeiro_nome = input("Digite seu primeiro nome: ")

tamanho_nome = len(primeiro_nome)

nome_pequeno = tamanho_nome <= 4
nome_normal = tamanho_nome == 5 or tamanho_nome == 6
nome_grande = tamanho_nome > 6

if nome_normal:
    print("seu nome é normal")
elif nome_pequeno:
    print('seu nome é muito curto')
elif nome_grande:
    print('seu nome é muito grande')
else:
    print('Voce digitou algo de errado')