class Animal:

    def run(self):
        print("Animal Running........")

    def eat(self):
        print("Animal eating.........")


class Cat(Animal):

    def meow(self):
        print("meow...........")


class Dog(Animal):

    def bark(self):
        print("Dog is barking...........")


dog = Dog()
dog.eat()
dog.run()
dog.bark()

cat = Cat()
cat.eat()
cat.run()
cat.meow()