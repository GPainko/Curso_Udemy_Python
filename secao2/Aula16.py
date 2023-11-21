#operadores sets

s1 = {1,2,3}

s2 = {2,3,4}

s3 = s1 | s2 # união
s4 = s1 & s2 # interseção
s5 = s1 - s2 # diferença
s6 = s2 - s1 # diferença
s7 = s1 ^ s2 # diferença simetrica

print(s3)
print(s4)
print(s5)
print(s6)
print(s7)