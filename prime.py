def prime(num):
    if num >1:
        for i in range(2,num):
            if num%i==0:
                print("not prime")
                break
        else:
            print("This is prime")
    else:
        print("plesse grwter number dal")
num=int(input("Enter Any number"))
prime(num)