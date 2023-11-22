#dir, hassattr e getattr em python

string = 'luiz'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string,metodo)())

