from observable import iPhoneObservable
from observer import emailAlertObserver, mobileAlertObserver

class MarketPlace:
    def __init__(self) -> None:
        # Add Code for Multiple Items Listing inside of class, so and so
        self.iPhone = iPhoneObservable.iPhoneObservable()

    def notifyEmail(self, email:str):
        observer = emailAlertObserver.EmailAlertObserver(emailId=email, observable=self.iPhone)
        self.iPhone.add(observer=observer)

    def notifyMobile(self, email:str):
        observer = mobileAlertObserver.MobileAlertObserver(emailId=email, observable=self.iPhone)
        self.iPhone.add(observer=observer)
    
    def setStockCount(self, newStocksAdded):
        self.iPhone.setStockCount(newStocksAdded)
    

if __name__ == '__main__':
    market = MarketPlace()

    market.notifyEmail('visheshsinha@icloud.com')
    market.notifyEmail('vishesh@aaatech.com')
    market.notifyMobile('visheshsinha@icloud.com')

    # notifies
    market.setStockCount(5)
    # Doesn't notifies
    market.setStockCount(5)
    # Doesn't notifies, makes the stock count 0
    market.setStockCount(-10)
    # notifies
    market.setStockCount(10)