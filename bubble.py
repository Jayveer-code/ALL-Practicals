#sort without using sort keyword
list=[11,54,22,67,21,90,76,33]
n=len(list)
for i in range(n):
    for j in range(i+1,n):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
        else:
            pass
            # print(list) use to show the operations steps in output 
print(list)



# from array import*
# ar1=array('i',[])
# n=int(input("Enter how many elementss in the array "))
# for i in range(n):
#     a=int(input("Enter Element"))
#     ar1.append(a)
# for i in range(n):
#     for j in range(i+1):
#         if(ar1[i]<ar1[j]):
#             temp=ar1[j]
#             ar1[j]=ar1[i]
#             ar1[i]=temp
# print("After the sorting elements is")
# for i in range(n):
#     print(ar1[i])