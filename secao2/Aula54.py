import json

# pessoa ={
#     'nome': 'Luiz Otavio',
#     'sobrenome': 'Miranda',
#     'enderecos':[
#         {'rua':'R1','numero':32},
#         {'rua':'R2','numero':55},
#     ],
#     'altura':1.8,
#     'numero_preferido':(2,4,6,8,10),
#     'dev':True,
# #     'nada':None,
# # }

with open('aula54.json','r') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))
    print(pessoa['nome'])
