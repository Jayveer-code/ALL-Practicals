from abc import ABC, abstractmethod

class Animal:
    @abstractmethod
    def sound(self):
        pass 
class Dog(Animal):
    def sound(self):
        return "Bow Bow"
class Cat(Animal):
    def sound(self):
        return "Mew Mew"
d=Dog()
c=Cat()
print("Cat is ...",c.sound())
print("Dog is ...",d.sound())