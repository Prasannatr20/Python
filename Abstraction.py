class Car:
    def __init__(self):
        self.acc= False # Not shown to user as it is not needed
        self.clutch= False # Not shown to user as it is not needed
    def start(self):
        self.clutch= True # Not shown to user as it is not needed
        self.acc= True # Not shown to user as it is not needed
        print("Car started")
car = Car()
car.start()