from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class ElectricVehicle(Vehicle):
    @abstractmethod
    def charge_battery(self):
        pass

class FuelVehicle(Vehicle):
    @abstractmethod
    def refuel(self):
        pass

class HybridVehicle(ElectricVehicle,FuelVehicle):

    def __init__(self,mode='electricity'):
        self.mode = mode
    
    def charge_battery(self):
        print('vehicle is in charging...')
    def refuel(self):
        print('vehicle is refilling...')
    def start_engine(self):
        print(f'engine is starting with {self.mode}')
    def switch_to_electric(self):
        self.mode = 'electricity'
        print(f'switched to {self.mode}')
    def switch_to_fuel(self):
        self.mode = 'fuel'
        print(f'switched to {self.mode}')


tesla = HybridVehicle()
tesla.charge_battery()
tesla.start_engine()
tesla.switch_to_fuel()
tesla.refuel()
tesla.start_engine()
tesla.switch_to_electric()
tesla.charge_battery()
tesla.start_engine()