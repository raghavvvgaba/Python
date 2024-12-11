class Car:
    brand = None
    model = None
    def __init__(self, brand, model):
        self.__brand = brand    # double underscore made private variable
        self.__model = model

    def fullName(self):
        print(self.__brand,self.__model) 

    def fuel_type(self):
        return "Petrol or Diesel"
    
    def get_brand(self):        # encapsulated it, andr kya hai nhi pta
        return self.__brand + "!"
    
    @staticmethod
    def description():
        return "Cars are amazing"
    
    @property    #will now be used as a property and cannot be changed
    def get_model(self):
        return self.__model

class ElectricCar(Car):
    battery_size = None
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):    #polymorphism
        return "Electric"   


e_car = ElectricCar("Tesla", "Model 3", 1000)
e_car.fullName()
e_car.get_brand()


print(Car.description())
my_car = Car("Bentley", "Continental GT")
print(my_car.get_model)