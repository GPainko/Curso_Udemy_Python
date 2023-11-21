#Exercicio - sistema de perguntas e respostas

perguntas = [
    {
        'Perguntas': 'Quanto é 2+2?',
        'Opções' : ['1','2','3','4'],
        'Resposta': '4',
    },
    {
        'Perguntas': 'Quanto é 5*5?',
        'Opções' : ['25','55','10','51'],
        'Resposta': '4',
    },
    {
        'Perguntas': 'Quanto é 10/2?',
        'Opções' : ['25','55','10','51'],
        'Resposta': '4',
    },

]

qtd_acertos = 0

for pergunta in perguntas:
    print('Pergunta: ', pergunta['Perguntas'])
    print()

    opcao = pergunta['Opções']

    for i, opcao in enumerate(opcao):
        print(f'{i})',opcao)

    escolha = input('Escolha uma opão:')


    acertou = False
    escolha_int = None
    qtd_opcao = len(opcao)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcao:
            if opcao[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        print('Acertou')
        qtd_acertos += 0
    else:
        print('errou')

    print()

print('voce acertou',qtd_acertos)
print('de',len(perguntas),'perguntas')
