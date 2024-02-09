# method vs @classmethod vs @staticmethod
# method - self, método de instancia
# @classmethod - cls, metodo de classe
# @staticmethod - método estático(sem self,sem cls)

class Connection:
    def __init__(self,host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self,user):
        #setter
        self.user = user

    def set_password(self,password):
        self.password = password

    @classmethod
    def crate_with_auth(cls,user,password):
        connection= cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print('Log:',msg)


# c1 = Connection()
# c1.set_user('Gui')
# c1.set_password(12345)
# print(c1.user,c1.password)
print(Connection.log('Essa é a mensagem de log'))
c1= Connection.crate_with_auth('luiz',98765)
print(c1.user)
print(c1.password)