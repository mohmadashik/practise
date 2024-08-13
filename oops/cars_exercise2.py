'''
1. Property Decorators
Modify the Car class to include a property age that calculates the car's age based on the current year and the year attribute.
'''
from datetime import datetime
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
    @property
    def age(self):
        return datetime.now().year - self.__year


maruthi = Car(model='maruthi',year=2016)
maruthi.display_info()
print(maruthi.age)