# Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
# Criar um sistema bancário (extremamente simples) que tem clientes, contas e
# um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
# possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

from abc import ABC, abstractmethod

# Define a classe Pessoa com getter para nome e idade
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

# Define a classe Cliente que herda de Pessoa
class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.__conta = None

    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self, conta):
        self.__conta = conta

# Define a classe Conta como uma classe abstrata

class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass

# Define a classe ContaCorrente que herda de Conta
class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo, limite):
        super().__init__(agencia, numero, saldo)
        self._limite = limite

    def sacar(self, valor):
        if valor <= self._saldo + self._limite:
            self._saldo -= valor
            return True
        return False

# Define a classe ContaPoupanca que herda de Conta
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            return True
        return False

#Define a classe Banco que agrega contas e clientes
class Banco:
    def __init__(self):
        self.__clientes = []
        self.__contas = []

    def adicionar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

    def autenticar(self, cliente, conta, agencia):
        if cliente not in self.__clientes:
            return False
        if conta not in self.__contas:
            return False
        if conta._agencia != agencia:
            return False
        return True

# Criação de objetos e execução
banco = Banco()
cliente1 = Cliente("João", 30)
conta_corrente = ContaCorrente(123, 321, 1000, 500)

cliente1.conta = conta_corrente
banco.adicionar_cliente(cliente1)
banco.adicionar_conta(conta_corrente)

if banco.autenticar(cliente1, conta_corrente, 123):
    print("Autenticação bem-sucedida!")
    conta_corrente.depositar(200)
    print("Saldo após depósito:", conta_corrente._saldo)
    if conta_corrente.sacar(500):
        print("Saque efetuado com sucesso.")
    else:
        print("Saldo insuficiente para o saque.")
    print("Saldo atual:", conta_corrente._saldo)
else:
    print("Falha na autenticação.")