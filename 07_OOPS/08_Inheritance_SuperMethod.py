# Super method is used to directly call a method from the parent class
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started..")
    @staticmethod
    def stop():
        print("Car stopped..")

class ToyotoCar(Car):       #to show inheritance, we write the class name 
    def __init__(self, name, type):
        self.name = name
        # self.type = type      #instead write code below
        super().__init__(type)

car1 = ToyotoCar("Etios", "electric")
print(car1.type)

# This ensures that parent class initializer is properly executed before extending it in the Child class.