# if / elif / else
# se / se não se / se não

entrada = input("Você quer 'entrar' ou 'sair'? ")

if entrada == "entrar":
    #bloco dentro do if
    print("você entrou no sistema")
elif entrada == "sair":
    #bloco dentro do elif
    print("você saiu do sistema")
else:
    #bloco dentro do else
    print("Você não digitou nem entrar e nem sair")
#fora do bloco