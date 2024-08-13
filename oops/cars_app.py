print('OOPS EXERCISES'.center(100,"*"))
''' Class and Object Creation:
        Define a class Car with attributes make, model, and year. Create an object of this class.'''

# class Car:
#     def __init__(self,make=None,model=None,year=None):
#         self.make = make
#         self.model = model 
#         self.year = year
# maruthi = Car()
# print('exercise 1')
# print(type(maruthi))
# # print(type(maruthi.__name__)) AttributeError: 'Car' object has no attribute '__name__'

'''
Methods in Class:

Add a method display_info() to the Car class that prints the car's details.
'''
# print('exercise 2')

# class Car:
#     def __init__(self,make=None,model=None,year=None):
#         self.make = make
#         self.model = model 
#         self.year = year
#         print(f'car object created :{self.model}')
#     def display_info(self):
#         print(f'car model : {self.model}')
# maruthi = Car(model='R15')
# maruthi.display_info()

'''
Constructor (init):

Define a constructor for the Car class that initializes the make, model, and year attributes.
'''
# print('exercise 3')
class Car:
    def __init__(self,make=None,model=None,year=None):
        self.make = make
        self.model = model 
        self.__year = year
        print(f'car object created :{self.model}')
    def display_info(self):
        print(f'car model : {self.model}')
    def get_year(self):
        return self.__year
maruthi = Car(model='R15')
maruthi.display_info()
'''

Inheritance:
Create a subclass ElectricCar that inherits from Car and has an additional attribute battery_size. Add a method describe_battery() to the subclass.
'''
# print('exercise 4')
# class ElectricCar(Car):
#     def __init__(self,battery_size):
#         print('ElectricCar initialized')
#         self.battery_size = battery_size
    
#     def describe_battery(self):
#         print(f'battery_size : {self.battery_size}')

# tesla = ElectricCar(battery_size=10)
# tesla.describe_battery()

'''
Method Overriding:

Override the display_info() method in the ElectricCar class to include the battery_size attribute in the output.
'''
print('exercise 5')
class ElectricCar(Car):
    def __init__(self,model=None,battery_size=None):
        print('ElectricCar initialized')
        self.battery_size = battery_size
        super().__init__(model=model)
    
    def describe_battery(self):
        print(f'battery_size : {self.battery_size}')
    
    def display_info(self):
        super().display_info()
        self.describe_battery()

tesla = ElectricCar(model='tesla',battery_size=10)
tesla.describe_battery()
tesla.display_info()

'''
Encapsulation:

Implement encapsulation by making the year attribute of the Car class private and providing a method to get its value.
'''
climber = Car(model='climber',year=2021)
# print(climber.__year) AttributeError: 'Car' object has no attribute '__year'
print(climber.get_year())
'''
Polymorphism:

Create another class Bike with a method display_info(). Write a function that takes a list of vehicles (both Car and Bike) and calls display_info() on each.
'''

class Bike:
    def __init__(self,make=None,model=None,year=None):
        self.make = make
        self.model = model 
        self.__year = year
        print(f'bike object created :{self.model}')
    def display_info(self):
        print(f'bike model : {self.model}')
    def get_year(self):
        return self.__year    

hero = Bike(model='hero',year=2015)

def display_info(vehicles):
    for vehicle in vehicles:
        vehicle.display_info()
vehicles = [hero,climber,tesla]

display_info(vehicles=vehicles)