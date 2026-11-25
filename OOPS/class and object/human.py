class Human:
    name=None
    age=None
    weight=None
    height=None

    def read(self):
        print(self.name,"is reading")

person1= Human()
person1.name="Jeeva"
person1.age=25
person1.weight=50
person1.height=5
person1.place="Chennai"  #In python we can directly create a class template(Property) while creatimg the object

person2 =Human()
person2.name="Sankaraiah"
person2.age=23
person2.weight=48
person2.height=5.5

print(person1.place)
person1.read()  #Here, the person1 will be passed as self key word in read method
person2.read()