class A:
    def method_A(self):
        print("Method A from class A")
class B(A):
    def method_B(self):
        super().method_A()

b1 = B()
b1.method_B()