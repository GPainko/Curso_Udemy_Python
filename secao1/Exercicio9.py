"""
Faça um jogo para usuário adivinhar qual a palavra secreta.
- você vai propor uma palavra secreta qualquer e vai dar a 
  possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai coferir 
  se a letra digitada está na palavra secreta.
    - se a letra digitada estiver na palavra secreta: exiba a letra:
    -se a letra digitada não estiver na palavra secreta: exiba *.
- faça a contagem de tentativas do seu usário.
"""

import os

palavra_secreta = "trabalho"
letras_acertadas = ''
numero_tentativas = 0

while True:

    numero_tentativas += 1
    letra_digitada = input('Digite uma letra:')
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('Você Ganhou!! PARABENS')
        print(f'a palavra era {palavra_secreta}')
        print(f'teu numero de tentativas foi {numero_tentativas}')
        numero_tentativas = 0
        letras_acertadas = ''
    