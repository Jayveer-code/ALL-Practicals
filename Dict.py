diction={"name":"jayu","Age":21}
print(diction["name"])
print(diction["Age"])
#2nd way to aCCESS THE DICTIONARY ELEMENTS
print(diction.get("name"))
print(diction.get("Age"))

class person:
    def __init__(self,name,sname,age):
        self.name=name
        self.sname=sname
        self.age=age
p=person("JayveerSinh","Chavda",21)
print("Name is",p.sname,p.name,p.age)

class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Bark")

d = Dog()
d.speak()
add=lambda x,y:x+y
total=0
for i in range(1, 16):
   total=add(total,i)
print(total)

print("Reverse String in python")
j="Jayveer"
print(j[::-1])