class Motor:
    def __init__(self, modelo):
        self.modelo = modelo
        self.carros = []  # Lista para manter os carros que usam este motor

    def adicionar_carro(self, carro):
        self.carros.append(carro)


class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []  # Lista para manter os carros fabricados por este fabricante

    def fabricar_carro(self, carro):
        self.carros.append(carro)
        carro.fabricante = self


class Carro:
    def __init__(self, nome, motor, fabricante=None):
        self.nome = nome
        self.motor = motor
        motor.adicionar_carro(self)  # Adiciona este carro à lista de carros do motor
        self.fabricante = fabricante
        if fabricante:
            fabricante.fabricar_carro(self)  # Adiciona este carro à lista de carros do fabricante

    def exibir_informacoes(self):
        print(f'Carro: {self.nome}')
        print(f'Motor: {self.motor.modelo}')
        if self.fabricante:
            print(f'Fabricante: {self.fabricante.nome}')


# Criando os objetos de motor e fabricante
motor_v8 = Motor('V8 Turbo')
ford = Fabricante('Ford')

# Criando o objeto carro
mustang = Carro('Mustang GT', motor_v8, ford)

# Exibindo as informações do carro
mustang.exibir_informacoes()