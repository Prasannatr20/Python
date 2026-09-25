# class Car:
#     def __init__(self):
#         self.acc= False # Not shown to user as it is not needed
#         self.clutch= False # Not shown to user as it is not needed
#     def start(self):
#         self.clutch= True # Not shown to user as it is not needed
#         self.acc= True # Not shown to user as it is not needed
#         print("Car started")
# car = Car()
# car.start()


#Practise

class Account:
    def __init__(self, accNum, balance):
        self.accNum= accNum
        self.balance= balance
    def debit(self, amount):
        if self.balance>=amount:
            self.balance-=amount
            print("Amount debited successfully. New balance is:",self.balance)
        else:
            print("Insufficient balance, your balance is ", self.balance)
    def credit(self, amount):
        self.balance+=amount
        print("Amount credited successfully. New balance is:",self.balance)
    def check_balance(self):
        print("Your current balance is:",self.balance)
a1=Account(1234567890,5000)
a1.accNum
a1.balance
a1.credit(5000)
a1.debit(8000)
a1.check_balance()