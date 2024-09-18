# Abstract Vehicle system

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def fuel_type(self):
        pass
    

class Car(Vehicle):
    def __init__(self,brand, fuel):
        self.brand = brand
        self.fuel = fuel
        
    def move(self):
        return f"The car {self.brand} moves on four wheels"
    
    def fuel_type(self):
        return f"The car's fuel is {self.fuel}"
    
    
class Bike(Vehicle):
    def __init__(self, brand, fuel):
        self.brand = brand
        self.fuel = fuel
        
    def move(self):
        return f"The Bike {self.brand} moves on two wheels"
    
    def fuel_type(self):
        return f"The Bike's fuel is {self.fuel}"
    
class Boat(Vehicle):
    def __init__(self, brand, fuel):
        self.brand = brand
        self.fuel = fuel
        
    def move(self):
        return f"The boat {self.brand} moves on water"
    
    def fuel_type(self):
        return f"The boat's fuel is {self.fuel}"
    
    
    
vehicle1 = Car(input("Enter car brand: "), input("Enter the fuel type: "))
print(vehicle1.move())
print(vehicle1.fuel_type())

vehicle2 =  Bike(input("Enter Bike brand: "), input("Enter the fuel type: "))
print(vehicle2.move())
print(vehicle2.fuel_type())

vehicle3 = Boat(input("Enter boat brand: "), input("Enter the fuel type: "))
print(vehicle3.move())
print(vehicle3.fuel_type())