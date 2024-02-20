from dataclasses import dataclass, field, fields


@dataclass
class Pessoa:
    nome: str = field(
        default='Missing',repr = False
    )
    sobrenome: str = 'Not sent'
    idade: int = 0
    endereco : list[str] = field(default_factory=list)

if __name__ == '__main__':
    p1 = Pessoa('Luiz','Otávio')
    p2 = Pessoa()
    print(p1)
    print(p2)
    print(fields(p1))