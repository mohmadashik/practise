from abc import ABC,abstractmethod 
class Animal(ABC):
    @abstractmethod 
    def make_sound(self):
        pass 

class Dog(Animal):
    def make_sound(self):
        print('Bhow Bhow')

class Cat(Animal):

    def make_sound(self):
        print('meow')


tom = Cat()
scooby = Dog()

tom.make_sound()
scooby.make_sound()