class Student:
    college_name = "Manipal"    #class attributes
    name = "Anonymous"          #class attributes
    def __init__(self, fullname, marks):
        self.name = fullname            #instance attributes
        self.marks = marks              #instance attributes

s1 = Student("Karan", 97)
print(s1.name, s1.marks, s1.college_name, Student.name)

s2 = Student("Priyansh", 88)
print(s2.name, s2.marks, Student.college_name)