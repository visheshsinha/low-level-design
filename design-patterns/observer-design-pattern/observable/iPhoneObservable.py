# import sys
# sys.path.append("..")

from observer import notificationAlertObserver
from observable import stocksObservable


class iPhoneObservable(stocksObservable.StockObservable):
    def __init__(self) -> None:
        self.observerList = {}
        self.stockCount = 0

    def add(self, observer: notificationAlertObserver.NotificationAlertObserver):
        print(f'Adding Observer {observer} into list')
        self.observerList[observer] = True
    
    def remove(self, observer: notificationAlertObserver.NotificationAlertObserver):
        print(f'Removing Observer {observer} from list')
        del self.observerList[observer]

    def notifyObservers(self):
        for observer in self.observerList.keys():
            print(f'Notifying {observer} from list')
            observer.update()
    
    def setStockCount(self, newStocksAdded: int):
        print(f'Updating Stock Count in Observable')
        if self.stockCount == 0:
            self.notifyObservers()
        
        self.stockCount += newStocksAdded
    
    def getStocksCount(self):
        return self.stockCount