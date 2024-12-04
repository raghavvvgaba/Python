#Methods are functions that belongs to objects
class Student:
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
    def hello(self):
        print("hello", self.name)
    def get_marks(self):
        return self.marks

s1 = Student("Karan", 97)
s1.hello()
print(s1.get_marks())