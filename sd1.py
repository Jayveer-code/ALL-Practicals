# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def swagat(self):
#         print("Welcome At Aims Achivers...",self.name)
        
#     def getmarks(self):
#         return self.marks    
    
# s1=student("Jayveer",98)
# s1.swagat()
# print(s1.name,"Your maks is ",s1.marks)

# s2=student("Sunderpichai",97)
# print(s2.name,"Your maks is ",s2.marks)
# s2.swagat()
# if s1.marks >= s2.marks:
#     print("=============================")
#     print("Jayveer is CEO of Google")
#     print("=============================")
# else:
#     print("Sp is CEO of Google") 
# print("=============================")
# print(s1.getmarks())
# print(s2.getmarks())
# print("=============================")

#prctice Quetion 
# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
#     def Avg(self):
#         sum=0
#         for val in self.marks:
#             sum += val
#             print("Hi",self.name,"Your average MArks is",sum/3)
# s1=student("jayveer",[98,97,99])
# s1.Avg()

#static methods without taking self veribles
class sudent:
    @staticmethod
    def hello():
        print("hell0")
c1=sudent()
c1.hello()