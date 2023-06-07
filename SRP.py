"""Single-responsibility principle (SRP)"""
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
    
class PaymentProcessor:
    def pay_debit(self, order, security_code):
        print('Processing debit payment type')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'
    
    def pay_credit(self, order, security_code):
        print('Processing credit payment type')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'
    

order = Order()
order.add_item("keyboard", 1, 50)
order.add_item("SSD", 3, 100)
order.add_item("USB", 1, 20)

print(order.total_price())
processor = PaymentProcessor()
processor.pay_credit(order, '123456') 
