# Parent class 1
class Father:
    def skills(self):
        print("I am good at driving.")

# Parent class 2
class Mother:
    def hobbies(self):
        print("I love painting.")

# Child class inheriting from both Father and Mother
class Child(Father, Mother):
    def talent(self):
        print("I am good at coding!")

# Using the Child class
child = Child()
child.skills()   # Output: I am good at driving.
child.hobbies()  # Output: I love painting.
child.talent()   # Output: I am good at coding!


class A:
    A = "Welcome to class A"

class B(A):  # Class B inherits from Class A
    B = "Welcome to class B"

class C(B):  # Class C inherits from Class B
    C = "Welcome to class C"

# Create an object of the last child class
c1 = C()

# Access attributes from all levels
print(c1.C)  # Output: Welcome to class C
print(c1.B)  # Output: Welcome to class B
print(c1.A)  # Output: Welcome to class A
