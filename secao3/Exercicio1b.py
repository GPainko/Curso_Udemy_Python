# carregar_classe.py
import json

class MinhaClasse:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

def carregar_instancia_de_json(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
        return MinhaClasse(**dados)

# Exemplo de uso
if __name__ == "__main__":
    nome_arquivo = "minha_classe.json"
    instancia_carregada = carregar_instancia_de_json(nome_arquivo)
    print(f"Nome: {instancia_carregada.nome}, Idade: {instancia_carregada.idade}")