We studied about three types of methods

1. Instance methods
Operate on instance variables of the class.
Require self as the first parameter to refer to the instance.

eg - class MyClass:
    def instance_method(self):
        print("This is an instance method.")


2. Class Methods
Operate on the class itself (not specific to instances).
Use @classmethod decorator and cls as the first parameter to refer to the class

eg - class MyClass:
    @classmethod
    def class_method(cls):
        print("This is a class method.")

3. Static Methods
Do not operate on instance or class variables.
Use @staticmethod decorator.
Behave like regular functions but belong to the class's namespace.

eg - class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")
