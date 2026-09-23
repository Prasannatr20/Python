class Factory:
    def __init__(self, product, brand):
        self.product = product
        self.brand= brand
f1= Factory("blue", "BMW")
print(f1.brand)
print(f1.product)