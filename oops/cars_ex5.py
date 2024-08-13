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
    
    # def __str__(self):
    #     return f'Car object with model {self.model}'
    
    def __repr__(self):
        return f'This is also Car object with model {self.model} using __repr__'


tesla = Car(model='tesla')
print(tesla)
    
