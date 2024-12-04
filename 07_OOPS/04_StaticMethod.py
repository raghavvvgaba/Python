# Methods that don't use the self parameter.  It is used for functionality that is related to the class but does not need access to instance-specific data (self) or class-level data
# eg - a hello function. A self doesn't make sense here

class Student:
    @staticmethod   #decorator
    def college():
        print("ABC college")


# A decorator takes in a function as parameter and modifies and then returns a function 
# It allows to wrap another function to extend its behaviour without permanently modifying it