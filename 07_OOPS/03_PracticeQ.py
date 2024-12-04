class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        avg = 0
        for i in self.marks:
            avg = avg + i
        # print("hi", self.name, "average score is ", avg/3)
        return avg/3
    
s1 = Student("Tony", [99,98,97])
print(s1.average())