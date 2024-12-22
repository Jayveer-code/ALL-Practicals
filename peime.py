# def prime(num):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 print(num," is not prime number")
#                 break
#         else:
#             print(num," is prime number")
#     else:
#         print("Enter number is lessthan xero please enter grater Number")
# num=int(input("Enter Number to check Prime Or not :: "))
# prime(num)

# print prime number under 1 to 100
print("There is all prime number between 1 to 100")
for num in range(2,101):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            break
    else:
        print(num,end=" ")
    




