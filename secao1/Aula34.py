# while/else

string = 'valor qualquer'

i = 0

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break 

    print(letra)
    i += 1

else:
    print('o else foi executado')
print('fora do while')