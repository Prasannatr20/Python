class Marks:
    name=None
    english=None
    maths= None
    physics=None
    chemistry=None
    biology=None

    def total(self):
        print(f"Total marks of {self.name} is=", self.biology+self.english+self.chemistry+self.maths+self.physics)
        return self.biology+self.english+self.chemistry+self.maths+self.physics


totalMarks=[]
student1 = Marks()
student1.name="Prasanna"
student1.english=60
student1.maths=80
student1.physics=80
student1.chemistry=77
student1.biology=89
totalMarks.append(student1.total())

student2 = Marks()
student2.name = "Karthik"
student2.english = 75
student2.maths = 92
student2.physics = 88
student2.chemistry = 84
student2.biology = 79
totalMarks.append(student2.total())

student3 = Marks()
student3.name = "Divya"
student3.english = 88
student3.maths = 76
student3.physics = 81
student3.chemistry = 85
student3.biology = 94
totalMarks.append(student3.total())

student4 = Marks()
student4.name = "Arjun"
student4.english = 64
student4.maths = 95
student4.physics = 91
student4.chemistry = 89
student4.biology = 72
totalMarks.append(student4.total())

student5 = Marks()
student5.name = "Meera"
student5.english = 91
student5.maths = 84
student5.physics = 79
student5.chemistry = 88
student5.biology = 92
totalMarks.append(student5.total())

student6 = Marks()
student6.name = "Vikram"
student6.english = 58
student6.maths = 73
student6.physics = 69
student6.chemistry = 74
student6.biology = 68
totalMarks.append(student6.total())

student7 = Marks()
student7.name = "Ananya"
student7.english = 85
student7.maths = 89
student7.physics = 90
student7.chemistry = 91
student7.biology = 87
totalMarks.append(student7.total())

student8 = Marks()
student8.name = "Siddharth"
student8.english = 72
student8.maths = 68
student8.physics = 74
student8.chemistry = 70
student8.biology = 76
totalMarks.append(student8.total())

student9 = Marks()
student9.name = "Kavya"
student9.english = 94
student9.maths = 88
student9.physics = 85
student9.chemistry = 90
student9.biology = 96
totalMarks.append(student9.total())

student10 = Marks()
student10.name = "Rohan"
student10.english = 67
student10.maths = 81
student10.physics = 77
student10.chemistry = 73
student10.biology = 80
totalMarks.append(student10.total())

max=totalMarks[0]
min=totalMarks[0]
for i in range(0,len(totalMarks)):    
    if totalMarks[i]>max:
        max=totalMarks[i]
    if totalMarks[i]<min:
        min=totalMarks[i]

print("Highest is ",max)
print("Best learner is ",min)