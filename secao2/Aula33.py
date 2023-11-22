# try, except , else e finalyy

try:
    print('Abrir arquivo')
    #8/0
except ZeroDivisionError:
    print('dividio por zero')
else:
    print('Não deu erro')
finally:
    print('Fechar arquivo')
