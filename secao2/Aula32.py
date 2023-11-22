#try, except , else, finally

a = 18
b = 0

try:
    c = a / b
except ZeroDivisionError as e:
    print(e)
    print(e.__class__.__name__)

except NameError:
    print('Variavel não definida')
except (IndexError,TypeError) as error:
    print('Typer erro + index error')
    print('MSG:', error)
    print('MSG:', error.__class__.__name__)
except Exception:
    print('Erro Descohecido')

print('Continuar')