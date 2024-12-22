# Base class
class Grandfather:
    def hobby(self):
        print("I love gardening.")

# Intermediate class inheriting from Grandfather
class Father(Grandfather):
    def skill(self):
        print("I am good at carpentry.")

# Child class inheriting from Father
class Son(Father):
    def talent(self):
        print("I am great at coding!")

# Using the classes
son = Son()
son.hobby()   # Output: I love gardening.
son.skill()   # Output: I am good at carpentry.
son.talent()  # Output: I am great at coding!

#Most simple exmaple of inheritance
class A:
    A="Welcome to clasd A"
class B:
    B="Welcome to clasd B"
class c(A,B):
    c="Welcome to class C"
c1=c()
print(c1.c)
print(c1.B)
print(c1.A)