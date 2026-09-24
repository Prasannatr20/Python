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
    @staticmethod
    def hello():
        print("Hello!")
    def get_marks(self):
        return "Marks of", self.name,"->", self.marks

s1= Student("Anbu", 88)
s1.hello()
print(s1.get_marks())