class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])

    def inserir_produtos(self,*produtos):
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()

class Produto:
    def __init__(self,nome,preco) -> None:
        self.nome = nome
        self.preco = preco


carinho = Carrinho()
p1,p2 = Produto('Caneta',1.20), Produto('Camiseta',34)
carinho.inserir_produtos(p1,p2)
carinho.listar_produtos()
print(carinho.total())