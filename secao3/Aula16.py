class Cliente:

    def __init__(self,nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua,numero):
        self.enderecos.append(Endereco(rua,numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('Apagando',self.nome)


class Endereco:
    def __init__(self,rua,numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('Apagando',self.rua,self.numero)


cliente = Cliente('Maria')
cliente.inserir_endereco('Av Madeira',54)
cliente.inserir_endereco('Rua B', 323)
cliente.listar_enderecos()

print('Fim do codigo')