# def palid(name):
#     name=name.lower()
#     name="".join(char for char in name if char.isalnum())
#     return name==name[::-1]
# name=input("Enter string")
# if palid(name):
#     print("This is paalid")
# else:
#     print("Not palid")


# l=[22,55,71,88,11,2]
# check=l[0]
# for num in l:
#     if num>check:
#         check=num
# print("The large is",check)


# name="jayveer"
# rs=""
# for char in name:
#     rs=char+rs
# print(rs)

# number=int(input("Enter number print multitable ::"))
# for i in range(1,11):
#     print(number,"X",i,"=",i*number)

# y=int(input("Enter year"))
# if(y %4==0 and y%100!=0)or(y%400==0):
#     print("leap year")
# else:
#     print("not leap year")

number=int(input("Enter number"))
fact=1
n=1
while n<=number:
    fact=fact*n
    n=n+1
print("the factorial is",fact)