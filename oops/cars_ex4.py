"""
3. Multiple Inheritance
Create another class Automobile with a method start_engine().
Make ElectricCar inherit from both Car and Automobile. Ensure there are no conflicts.
"""
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
        print(f'year : {self.__year}')
    @property
    def age(self):
        return datetime.now().year - self.__year

class AutoMobile:
    def __init__(self,engine_model=None):
        self.engine_model = engine_model
        print('Automobile class instantiated')
    
    def start_engine(self):
        print(f'Engine started: {self.engine_model}')


class ElectricCar(Car,AutoMobile):
    def __init__(self,name=None,year=None):
        self.name =name
        Car.__init__(self,year=year)
        AutoMobile.__init__(self,engine_model='67xA')


tesla = ElectricCar(name='tesla-100',year=2005)
tesla.start_engine()
tesla.get_year()


