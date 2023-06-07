"""Interface segregation principle (ISP)"""
from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = 'open'

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
    
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass
    
class PaymentProcessor_SMS(PaymentProcessor):
    @abstractmethod
    def auth_sms(self, code):
        pass

class DebitPaymentProcessor(PaymentProcessor_SMS):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False
    
    def auth_sms(self, code):
        print(f"Verifying SMS code: {code}")
        self.verified = True
    
    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        print('Processing debit payment type')
        print(f'Verifying security code: {self.security_code}')
        order.status = 'paid'

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print('Processing credit payment type')
        print(f'Verifying security code: {self.security_code}')
        order.status = 'paid'
    
class PaypalPaymentProcessor(PaymentProcessor_SMS):
    def __init__(self, email):
        self.email = email
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code: {code}")
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        print('Processing paypal payment type')
        print(f'Verifying email address: {self.email}')
        order.status = 'paid'
    

order = Order()
order.add_item("keyboard", 1, 50)
order.add_item("SSD", 3, 100)
order.add_item("USB", 1, 20)

# print(order.total_price())
# processor = CreditPaymentProcessor('123456')
# processor.pay(order) 

processor = PaypalPaymentProcessor('hi@example.com')
processor.auth_sms('1234')
processor.pay(order) 

# processor = DebitPaymentProcessor('123456')
# processor.auth_sms('1234')
# processor.pay(order) 
