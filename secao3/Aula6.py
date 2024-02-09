class Camera:
    def __init__(self,nome,filmando = False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):

        if self.filmando:
            print(f'{self.nome} já está filmando...\n')
            return 
        
        print(f'{self.nome} está filmando...\n')
        self.filmando = True

    def parafilmar(self):

        if not self.filmando:
            print(f'{self.nome} não está filmando...\n')
            return 
        
        print(f'{self.nome} está parando de filmar...\n')
        self.filmando = False
        

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando\n')
            return
        
        print(f'{self.nome} esta fotografando\n')


c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c1.filmar()
c1.fotografar()
c1.parafilmar()
c1.fotografar()

c2.fotografar()
c2.parafilmar()
c2.fotografar()

