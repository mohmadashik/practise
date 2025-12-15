print("Interview practise Python".center(80,"*"))

class Car:
	def __init__(self,name,make,model,year):
		self.name = name
		self.make = make  
		self.model = model
		self.year = year

	def __str__(self):
		return f'{self.name} is a {self.model} car,made in {self.make} in the year {self.year}'

maruthi = Car('maruthi-elite','India','Diesel',1973)
print()
print(maruthi)

#Abstration 
from abc import ABC,abstractmethod 

class Animal:
	# @abstractmethod
	def speak():
		pass 

class Dog(Animal):
	def speak(self):
		print('Bhow, Bhow')

class Cat(Animal):
	def speak(self):
		print('Meow, Meow')

jack = Dog()
jack.speak()
tom = Cat()
tom.speak()


#Class methods vs static methods

class Baker:

	count = 0

	@classmethod
	def increment(cls):
		cls.count+=1
		print(f'Class method : count incremented to : {cls.count}')


	@staticmethod
	def show_name(name):
		print(f"I'm a visiter and my name is {name}")
		# print(f"I'm trying to access class count property {count}") = this will throw error

Baker.increment()
Baker.increment()
Baker.show_name('AshikG')


class Singleton_Hero:
	_instance = None 
	def __new__(cls):
		if cls._instance is None: 
			cls._instance = super().__new__(cls)
		return cls._instance 

	def __str__(self):
		return "I'm a singleton hero"

spiderman = Singleton_Hero()
superman = Singleton_Hero()

print(spiderman)
print(superman)


class InvalidInput(Exception):
	def __init__(self):

		super().__init__("Invalid Input Bro, Need Integer")

a = '22432'
if type(a)!= int:
	raise(InvalidInput)

if type(a)!= int:
	raise(Exception('Invalid input bro, need integer'))

# **Both raise errors.

# But only custom exceptions give you clean handling, clean architecture, and clean debugging.**
