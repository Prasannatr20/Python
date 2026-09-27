class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def show(self):
        print(self.real, "i","+", self.img,"j")
    def __add__(self, num2):
        newreal= self.real + num2.real
        newimg= self.img + num2.img
        return Complex(newreal, newimg)

c1= Complex(2,3)
c2= Complex(4,5)
c3= c1 + c2
c3.show()