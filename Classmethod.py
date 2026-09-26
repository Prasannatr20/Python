#NormalMethod
# class Person:
#     name = "anonymous"

#     def change_name(self, name):
#         self.name= name #This changes the instance variable name but not the class variable
# p1 = Person()
# p1.change_name("Anbu")
# print(p1.name)
# print(Person.name)

#ClassMethod

class Person:
    name= "anonymous"

    @classmethod
    def changename(cls, name):
        cls.name= name #This changes the class variable name as it is a class method

p1 = Person()
p1.changename("Anbu")
print(p1.name)
print(Person.name)