import random


random.seed(3)#defini aleatoriedade

r_range = random.randrange(10,30)
print('randrange:')
print(r_range)
print()

r_int = random.randint(10,20)
print('randint')
print(r_int)
print()

r_uniform = random.uniform(10,20)
print('uniform')
print(f'{r_uniform:.2f}')
print()

nomes = ['Luiz','Maria','Carlos','João']
random.shuffle(nomes)
print('Shuffle')
print(nomes)
print()

novos_nomes = random.sample(nomes,k=2)
print('sample')
print(novos_nomes)
print()

novos_nomes = random.choices(nomes,k=3)
print('choices')
print(novos_nomes)
print()

print('choice')
print(random.choice(nomes))
print()

