class Employee:
    def __init__(self, dept, sal):
        self.dept= dept
        self.sal= sal
    def showEmpDetails(self):
        print(self.dept, self.sal)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name= name
        self.age = age
        super().__init__("AI Dev", 450000)
    def showEngDetails(self):
        print(self.name, self.age)
e1= Engineer("Prasanna", 23)
e1.showEmpDetails()
e1.showEngDetails()