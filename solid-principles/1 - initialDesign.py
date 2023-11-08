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
        
if __name__ == '__main__':
    newOrder = Order()
    newOrder.addItems('Keyboards', 23, 2.0)
    newOrder.addItems('Mouse', 17, 1.0)
    newOrder.addItems('Moniter', 5, 5.5)
    
    print(newOrder.totalPrice())
    newOrder.pay('debit', 'zbx01d')