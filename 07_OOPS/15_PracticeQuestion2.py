class Employee: 
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    def showDetails(self):
        print(self.role)
        print(self.department)
        print(self.salary)

class Engineer(Employee): 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "CS", "1,00,000")

eng1 = Engineer("Aaryan", 22)
eng1.showDetails()