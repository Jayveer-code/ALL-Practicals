class bank:
    
    def __init__(self,ano,apass):
        self.ano=ano
        self.password=apass
        self.balance=0
            
    def credit(self,amt):
        self.amt=amt
        self.balance+=amt
        print("Your account is credited balance is ",self.balance)

    def deposit(self,amt):
        self.balance-=amt
        print("Your account is debited balance is ",self.balance)

b1=bank(123135,"jayveersinh")
b1.credit(5000)        
b1.deposit(3000)
b1.credit(5000)  
        