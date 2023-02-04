from abc import *

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Every Animal Sleeps. So I am Common in All Animals")


class Dog(Animal):
    def sound(self):
        print("I Bark")

    def eat(self):
        print("I Eat Cat and Mouse")

class Lion(Animal):
    def sound(self):
        print("I can roar")

    def eat(self):
        print("I can only Eat Animals")

dog = Dog()
dog.sound()
dog.eat()
dog.sleep()


lion = Lion()
lion.sound()
lion.eat()
lion.sleep()