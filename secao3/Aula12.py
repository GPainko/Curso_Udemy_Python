# class Caneta:
#     def __init__(self,cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('\nGET COR')
#         return self.cor_tinta

# caneta = Caneta('Vermelho')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())

class Caneta:
    def __init__(self,cor):
        self.cor_tinta= cor

    @property
    def cor(self):
        print('\nPROPERTY')
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return 12345

caneta = Caneta('Vermelho')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)