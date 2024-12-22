try:
    x=10/0
except ZeroDivisionError as e:
    print("The x can not divide by 0",e)