class Bank:
    def __init__(self,account,balance):
        self.account=account
        self.balance=balance
        
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount ,"Was debited","Your total balance is",self.get_balance())
    
    
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount ,"Was credited","Your total balance is",self.get_balance())
        
    def get_balance(self):
        return self.balance
b1=Bank(8931402,12000)  #we can also add more accounts Their add more detils
print("Your Main balance is ",b1.balance)
b1.credit(5000)
b1.debit(2000)
