# just a normal class with instance attributes and methods but not an abstract class
class car:
    def __init__(self):
        self.accelator=False
        self.start=False
        self.breks=False
    def statt(self):
        self.accelator=True
        self.start=True
        print("The Car is start")
c1=car()
c1.statt()