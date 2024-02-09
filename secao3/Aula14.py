class Foo:
    def __init__(self):
        self.public = 'isso é public'
        self._protected = 'isso é protegido'# conveção em python 
        self.__private = 'isso é privado'

    def metodo_publico(self):
        return 'Metodo_publico'

    def _metodo_protegido(self):
        return '_metodo_protegido'

    def __metodo_privado(self):
        return '__metodo_privado'

f = Foo()
print(f.public)
print(f.metodo_publico())
