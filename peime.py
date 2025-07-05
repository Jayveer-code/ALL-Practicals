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

def prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print("this is not prime")
                break
        else:
            print("it is prime")
    else:
        print("number is less to zero")
prime(14)

