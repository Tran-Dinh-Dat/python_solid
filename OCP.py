"""Open-closed principle (OCP)"""
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
    def pay(self, order, security_code):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print('Processing debit payment type')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'

class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print('Processing credit payment type')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'
    
class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print('Processing paypal payment type')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'
    

order = Order()
order.add_item("keyboard", 1, 50)
order.add_item("SSD", 3, 100)
order.add_item("USB", 1, 20)

print(order.total_price())
processor = PaypalPaymentProcessor()
processor.pay(order, '123456') 
