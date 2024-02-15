class MeuError(Exception): 
    ...


class OutroError(Exception): 
    ...


def levantar():
    exception_ = MeuError('A','B','C')
    exception_.add_note('Olha a nota 1')
    raise exception_


try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Vou lançar de novo')
    exception_.add_note('Mais uma nota')
    exception_.__notes__ += error.__notes__.copy()
    raise exception_ from error