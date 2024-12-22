class A:
    def dis(self):
        print("This is parent class")
class B(A):
    def dis(self):
        print("This is child class")
b1=B()
b1.dis()