from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def milage(self):
        pass


class Tesla(Car):

    def milage(self):
        print("Milage of tesla cae is 30km")


class Suzuki(Car):

    def milage(self):
        print("Milage of Suzuki cae is 20km")


t = Tesla()
t.milage();

s = Suzuki()
s.milage()