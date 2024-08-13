'''
2. Class Variables
Add a class variable num_of_cars to the Car class that keeps track of the number of car objects created. 
Increment this variable each time a new car object is created.
'''

from datetime import datetime
class Car:
    num_of_cars = 0
    def __init__(self,make=None,model=None,year=None):
        self.make = make
        self.model = model 
        self.__year = year
        Car.num_of_cars+=1
        print(f'car object created :{self.model}')
        print(f'no of cars : {Car.num_of_cars}')

    def display_info(self):
        print(f'car model : {self.model}')
    def get_year(self):
        return self.__year
    @property
    def age(self):
        return datetime.now().year - self.__year

maruthi = Car(model='maruthi',year=2016)
nano = Car(model='nano',year=2015)
climber = Car (model='climber',year=2021)
# maruthi.display_info()
# print(maruthi.age)