class Student:
    def __init__(self, name, marks):
        self.name= name
        self.marks= marks
    def avg(self):
        totalMarks= 0
        for i in self.marks:
            totalMarks += i
        return totalMarks/len(self.marks)

s1= Student("Anbu", [88,90,93,83,80])
print(s1.avg())