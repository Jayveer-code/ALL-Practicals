# class A:
#     def __init__(self,acno,password):
#         self.ano=acno
#         self.__password=password
# a1=A("575757","576857")
# print(a1.ano)
# print(a1.__password)#this gives eeror beacuse its a prive not accesibble in otside thw class

#For Access this we use in another class

class A:
    def __init__(self,acno,password):
        self.ano=acno
        self.__password=password
        
    def rest_pass(self):
        print(self.__password)
a1=A("575757","576857")
print("This is account number  ",a1.ano)
print("This is password  ")
print(a1.rest_pass())