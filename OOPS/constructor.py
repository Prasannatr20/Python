class Student:
    def __init__(self):
        self.name=""
        self.reg_num=0
    def display(self):
        print(self.name)
        print(self.reg_num)

student1=Student()
student1.name="Asura"
student1.reg_num=1
student1.display()