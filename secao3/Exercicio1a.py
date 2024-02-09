# salvar_classe.py
import json

class MinhaClasse:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def para_json(self):
        return json.dumps(self.__dict__)

def salvar_instancia_em_json(instancia, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(instancia.para_json())

# Exemplo de uso
if __name__ == "__main__":
    instancia = MinhaClasse("João", 25)
    nome_arquivo = "minha_classe.json"
    salvar_instancia_em_json(instancia, nome_arquivo)