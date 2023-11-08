from abc import ABC, abstractmethod

# One Resposibility - Order Status & All
class Order:
    def __init__(self) -> None:
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = 'OPEN'

    def addItems(self, name: str, quantity: int, price: float):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
    
    def totalPrice(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.prices[i] * self.quantities[i]
        
        return total
    
    def pay(self, paymentType: str, securityCode: str):
        if paymentType == 'debit':
            print('Processing Debit Payment Type')
            print(f'Verifying Security Code: {securityCode}')
            self.status = 'PAID'
        elif paymentType == 'credit':
            print('Processing Credit Payment Type')
            print(f'Verifying Security Code: {securityCode}')
            self.status = 'PAID'
        else:
            raise Exception(f'Unkown payment type: {paymentType}')



# One Resposibility - Payment Processing & All
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order):
        pass

# Several Specific Interfaces
class PaymentProcessor_SMS(PaymentProcessor):
    @abstractmethod
    def authSMS(self, code):
        pass

# Using Composition, instead of more sub-classes -- more helpful
class SMSAuth:
    def __init__(self) -> None:
        self.authorized = False
    
    def verifyCode(self, code):
        print(f'Verifying Code: {code}')
        self.authorized = True
    
    def isAuthorized(self) -> bool:
        return self.authorized

# Open - Extension of a particular payment method
# Close - Modification 
class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, securityCode, authorizer: SMSAuth) -> None:
        self.authorizer = authorizer
        self.securityCode = securityCode

    def pay(self, order: Order):
        if not self.authorizer.isAuthorized():
            raise Exception('NOT AUTHORISED - 401')

        print('Processing Debit Payment Type')
        print(f'Verifying Security Code: {self.securityCode}')
        order.status = 'PAID'
        
class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, securityCode, authorizer: SMSAuth) -> None:
        self.authorizer = authorizer
        self.securityCode = securityCode

    def pay(self, order: Order):
        if not self.authorizer.isAuthorized():
            raise Exception('NOT AUTHORISED - 401')

        print('Processing Credit Payment Type')
        print(f'Verifying Security Code: {self.securityCode}')
        order.status = 'PAID'

class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, emailAddress) -> None:
        self.emailAddress = emailAddress

    def pay(self, order: Order):
        print('Processing Paypal Payment Type')
        print(f'Verifying Email Address: {self.emailAddress}')
        order.status = 'PAID'


if __name__ == '__main__':
    newOrder = Order()
    newOrder.addItems('Keyboards', 23, 2.0)
    newOrder.addItems('Mouse', 17, 1.0)
    newOrder.addItems('Moniter', 5, 5.5)
    
    print(newOrder.totalPrice())

    authorizer = SMSAuth()

    processor = DebitPaymentProcessor('x01adzb337l', authorizer)
    authorizer.verifyCode('793128')
    processor.pay(newOrder)

    processor = PaypalPaymentProcessor('visheshsinha@icloud.com')
    processor.pay(newOrder)