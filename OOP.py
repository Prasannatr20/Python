# class Factory:
#     def __init__(self, product, brand):
#         self.product = product
#         self.brand= brand
# f1= Factory("blue", "BMW")
# print(f1.brand)
# print(f1.product)


class Student:
    collegeName="Govt college"
    name= "No name"
    def __init__(self, name, marks):
        self.name= name
        self.marks= marks
    def hello(self):
        print("Hello,",self.name)
    def marks(self):
        return "Marks of", self.name

s1= Student("Anbu", 88)
s1.hello()
print(s1.marks())