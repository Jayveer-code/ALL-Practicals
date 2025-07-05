# single Inheritance Example
# class car:
#     color="white"
#     @staticmethod
#     def stat():
#         print("Car was started")
#     @staticmethod
#     def stop():
#         print("Car was stop")
# class Kiacars(car):
#     def __init__(self,name):
#         self.name=name
# c1=Kiacars("Benz")
# print(c1.color)


#multilevel inheritance
# class car:
#     color="white"
#     @staticmethod
#     def stat():
#         print("Car was started")
#     @staticmethod
#     def stop():
#         print("Car was stop")
# class Kiacars(car):
#     def __init__(self,brand):
#         self.brand=brand
        
# class fortuner(Kiacars):
#     def __init__(self,type):
#         self.type=type
# c1=fortuner("desiel")
# c1.stat()
# print(c1.brand)

class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):# overrides
        super().show()
        print("Child")

obj = Child()
obj.show()  # Output: Child