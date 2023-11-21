# exemplo de uso set

letras = set()

while True:
    letra = input('Digite sua letra: ')
    if len(letra) == 1:
        letras.add(letra.lower())

    if 'l' in letras:
        print('PARABENS')
        break

    print(letras)