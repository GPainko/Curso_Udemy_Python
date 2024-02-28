from time import sleep
from threading import Thread


# class MeuThread(Thread):
#     def __init__(self,texto,tempo):
#         self.texto = texto
#         self.tempo = tempo

#         super().__init__()

#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)


# t1 = MeuThread('Thread 1',5)
# t1.start()

# t2 = MeuThread('Thread 2',6)
# t2.start()

# t3 = MeuThread('Thread 3',7)
# t3.start()


# for i in range(200):
#     print(i)
#     sleep(1)


def vai_demorar(texto,tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar,args=('Olá mundo',2))
t1.start()
t1.join()

# while t1.is_alive():
#     print()
#     print('Esperando a thread')
#     sleep(2)

print('Thread acabou')
# t2 = Thread(target=vai_demorar,args=('Como Vai O mundo',5))
# t2.start()

# t2 = Thread(target=vai_demorar,args=('Tchau mundo',7))
# t2.start()

# for i in range(20):
#     print(i)
#     sleep(.5)