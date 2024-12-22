class account:
    def __init__(self,ano,acpass):
        self.ano=ano
        self.__acpass=acpass #This is Private only Accesible in the under class only
        
    def reset_pass(self):
        print(self.__acpass)
        
ac1=account("12345","5768")
print(ac1.ano)
print(ac1.reset_pass())