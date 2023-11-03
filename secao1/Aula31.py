contador = 0

while contador < 10:
    contador +=1

    if contador == 4:
        continue #volta para o inicio do laço  
    
    print(contador)

    if contador == 8:
        break # finaliza o laço


print('acabou')