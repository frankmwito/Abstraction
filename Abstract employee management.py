# Abstract employee management

from abc import ABC, abstractmethod

# Abstract Employee Class
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    
    def get_details(self):
        return f"Employee Name: {self.name}, Position: {self.position}"

# FullTimeEmployee Class
class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        self.name = name
        self.base_salary = base_salary
        self.bonus = bonus
        self.position = "Full Time"
    
    def calculate_salary(self):
        return f"Total Salary (Base + Bonus): {self.base_salary + self.bonus}"

# PartTimeEmployee Class
class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.position = "Part Time"
    
    def calculate_salary(self):
        return f"Total Salary (Hourly Rate * Hours Worked): {self.hourly_rate * self.hours_worked}"

# Freelancer Class
class Freelancer(Employee):
    def __init__(self, name, project_fee):
        self.name = name
        self.project_fee = project_fee
        self.position = "Freelancer"
    
    def calculate_salary(self):
        return f"Total Salary (Project Fee): {self.project_fee}"

# Creating instances and calculating salaries
employee1 = FullTimeEmployee(input("Enter full-time employee name: "), float(input("Enter base salary: ")), float(input("Enter bonus: ")))
print(employee1.get_details())
print(employee1.calculate_salary())

employee2 = PartTimeEmployee(input("Enter part-time employee name: "), float(input("Enter hourly rate: ")), int(input("Enter hours worked: ")))
print(employee2.get_details())
print(employee2.calculate_salary())

employee3 = Freelancer(input("Enter freelancer name: "), float(input("Enter project fee: ")))
print(employee3.get_details())
print(employee3.calculate_salary())
