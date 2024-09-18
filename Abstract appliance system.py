# Abstract Appliance System

from abc import ABC, abstractmethod

# Abstract Appliance Class
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

# Washing Machine Class
class WashingMachine(Appliance):
    def turn_on(self):
        return "The washing machine has electrical issues"
    
    def turn_off(self):
        return "The washing machine does a good job"

# Refrigerator Class
class Refrigerator(Appliance):
    def turn_on(self):
        return "The refrigerator is in good working condition"
    
    def turn_off(self):
        return "The refrigerator has a problem"

# Air Conditioner Class
class AirConditioner(Appliance):
    def turn_on(self):
        return "The air conditioner is working"
    
    def turn_off(self):
        return "The air conditioner is not working"

# Create instances and call methods
appliance1 = WashingMachine()
print(appliance1.turn_on())
print(appliance1.turn_off())

appliance2 = Refrigerator()
print(appliance2.turn_on())
print(appliance2.turn_off())

appliance3 = AirConditioner()
print(appliance3.turn_on())  # Fixed: Added parentheses
print(appliance3.turn_off()) # Fixed: Added parentheses
  