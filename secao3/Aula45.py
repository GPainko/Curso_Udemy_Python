from collections.abc import Sequence
from typing import Iterator

class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self,*values):
        for value in values:
            self._data[self._index] = value
            self._index +=1

    def __len__(self):
        return self._index
    
    def __getitem__(self,index):
        return self._data[index]
    
    def __setitem__(self,index,value):
        self._data[index] = value


    def __iter__(self):
        return self
    
    def __next__(self):
        if self._next_index >= self._index:
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value

if __name__ == '__main__':
    lista = MyList()
    lista.append('Maria')
    lista[0] = 'João'
    lista.append('Luiz')
    print(lista._data)

    for item in lista:
        print(item)