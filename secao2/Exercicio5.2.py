def primeiro_duplicado(lista):
    numeros_vistos = set()
    for numero in lista:
        if numero in numeros_vistos:
            return numero
        numeros_vistos.add(numero)
    return -1

# Exemplo de uso da função
if __name__ == "__main__":
    lista_exemplo1 = [1, 2, 3, 3, 2, 1]
    print(f"Primeiro duplicado: {primeiro_duplicado(lista_exemplo1)}")

    lista_exemplo2 = [1, 2, 3, 4, 5, 6]
    print(f"Primeiro duplicado: {primeiro_duplicado(lista_exemplo2)}")

    lista_exemplo3 = [1, 4, 9, 8, 9, 4, 8]
    print(f"Primeiro duplicado: {primeiro_duplicado(lista_exemplo3)}")