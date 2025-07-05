# num=int(input("Enter any numner"))
# fact=1
# n=1
# while n<=num:
#     fact=fact*n
#     n=n+1
# print("The factorial of",num,"is",fact)
# def check_odde(number):
#     result="even" if number%2==0 else "odd"
#     print(f"{number} is {result} number")
# check_odde(11)
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))