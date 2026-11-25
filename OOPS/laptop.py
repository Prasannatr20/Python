class Laptop:
    price=None
    processor=""
    ram=""

hp=Laptop()
dell=Laptop()
lenovo=Laptop()

hp.price=40000
hp.processor="i3"
hp.ram="8GB"

dell.price=60000
dell.processor="i5"
dell.ram="16GB"

lenovo.price=80000
lenovo.processor="i7"
lenovo.ram="32GB"

print(hp.price)
print(hp.processor)
print(hp.ram)
print("--------------")
print(dell.price)
print(dell.processor)
print(dell.ram)
print("---------------")
print(lenovo.price)
print(lenovo.processor)
print(lenovo.ram)


class Kodaikanal:
    regName=""
    def gunaCaves(self):
        print("Visited guna caves")
    def poondi(self):
        print("Visited poondi")
    def chocolates(self):
        print("Pruchased chocloates")

person1=Kodaikanal()
person1.regName="Vinayak"
print(person1.regName)
person1.gunaCaves()
person1.chocolates()
person2=Kodaikanal()
person2.regName="Jagdeesh"
print(person2.regName)
person2.poondi()
person2.gunaCaves()