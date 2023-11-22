# Introdução as generator functions em Python
# generator = (n for n in range(1000000))


def generator(n=0 , maximun = 10):

    while True:
        yield n

        n += 1

        if n > maximun:
            return


gen = generator(maximun = 1000000)

for n in gen:
    print(n)