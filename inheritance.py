#Single Inheritance
# class Car:
#     def start(self):
#         print("Car started")
#     def stop(self):
#         print("Car stopped")
# class ToyotaCar(Car):
#     pass
# t1= ToyotaCar()
# t1.start()
# t1.stop()

#Multi level Inheritance

# class Car:
#     def start(self):
#         print("Car started")
#     def stop(self):
#         print("Car stopped")
# class brand(Car):
#     def brand_name(self):
#         print("Brand name is Toyota")
# class color(brand):
#     def color_name(self):
#         print("Color name is Red")

# b1= color()
# b1.start()
# b1.brand_name()
# b1.stop()
# b1.color_name()

#Multiple Inheritance

class A:
    def method_A(self):
        print("Method A from class A")
class B:
    def method_A(self):
        print("Method B from class B")
class C(A,B):
    def method_C(self):
        print("Method C from class C")
c1= C()
c1.method_A()
#c1.method_B()
c1.method_C()
print(C.__mro__)
