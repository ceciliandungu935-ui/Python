class Animal:

    IsMammal = True
    hasFur = True

class Dog(Animal):
    def bark (self):
        print("Woof!! , Woof!!")

class Cat(Animal):
    def meow(self):
        print("Meow! Meow!")