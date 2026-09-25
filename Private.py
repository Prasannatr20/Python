class Person:
    def __hello(self):
        print("Hello, I am a person.")
    def welcome(self):
        self.__hello()
        print("welcome")
p1 = Person()
p1.welcome()