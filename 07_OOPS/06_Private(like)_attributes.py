# Private attributes & methods are meant to be used only within the class and are not accessible outside the class

# to create a private attribute or method, we just double underscore before it. It is also accessed by using double underscore only

class Person:
    __name = "anonymous"

    def __hello(self):
        print("Hello person!")

    def welcome(self):
        self. __hello()

p1 = Person()
print(p1.welcome())