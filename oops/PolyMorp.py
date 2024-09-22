# method overloading
# method overriding

class Animal():

    def speak(self):
        print("Animal is speaking........")


class Dog(Animal):

    def speak(self):
        print("Dog is barking........")


class Cat(Animal):

    def speak(self):
        print("Dog is meow........")


dog = Dog()
dog.speak()