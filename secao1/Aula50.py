#Lista de listas e sus indices

salas = [
    #0         1
    ['Maria','Helena'], # 0
    #0
    ['Elanine'], #1
    #0       1        2        
    ['Luiz','João','Eduarda'], #2
]

#print(salas[0][1])
#print(salas[1][0])
#print(salas[2][2])

for sala in salas:
    print(f'sala é {sala}')
    for aluno in sala:
        print(aluno)