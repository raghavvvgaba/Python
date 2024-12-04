class Car:
    @staticmethod
    def start():
        print("Car started..")
    @staticmethod
    def stop():
        print("Car stopped..")

class ToyotoCar(Car):       #to show inheritance, we write the class name 
    def __init__(self, name):
        self.name = name

car1 = ToyotoCar("Land Cruiser")
car2 = ToyotoCar("Supra")

car1.start()


#types of inheritance 
# 1. Single inheritance -> One base class derived from one derived class

# 2. Multi-level -> base se derived se derived

# 3. Multiple Inheritance -> deriving multiple classes to one child class eg-> class A and class B can be derived in class C like this -- class C(A,B)

class Fortuner(ToyotoCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("Diesel")
car1.start()

