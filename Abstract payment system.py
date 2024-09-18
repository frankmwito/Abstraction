# Abstract payment system

from abc import ABC, abstractmethod

# Abstract class Payment
class Payment(ABC):
    @abstractmethod
    def make_payment(self):
        pass

# CreditCardPayment class
class CreditCardPayment(Payment):
    def __init__(self, card_number, amount):
        self.card_number = card_number
        self.amount = amount
    
    def make_payment(self):
        return f"Your credit card payment of {self.amount} from card number {self.card_number} was successful."

# PayPalPayment class
class PayPalPayment(Payment):
    def __init__(self, email, amount):
        self.email = email
        self.amount = amount
    
    def make_payment(self):
        return f"Your PayPal payment of {self.amount} from account {self.email} was successful."

# CashPayment class
class CashPayment(Payment):
    def __init__(self, amount):
        self.amount = amount
    
    def make_payment(self):
        return f"Your cash payment of {self.amount} was successful."

# Simulate different payments
payment1 = CreditCardPayment(int(input("Enter your credit card number: ")), float(input("Enter the amount: ")))
print(payment1.make_payment())

payment2 = PayPalPayment(input("Enter your PayPal email: "), float(input("Enter the amount: ")))
print(payment2.make_payment())

payment3 = CashPayment(float(input("Enter the amount for cash payment: ")))
print(payment3.make_payment())
