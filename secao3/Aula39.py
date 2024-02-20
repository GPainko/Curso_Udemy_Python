from dataclasses import dataclass

@dataclass
class Pessoa:
    nome:str
    sobrenome:str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self,valor):
        nome,*sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Luiz','Soares')
    p1.nome_completo = 'João Carlos de alcantra'
    print(p1)
    print(p1.nome_completo)
