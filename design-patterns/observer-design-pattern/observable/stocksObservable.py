from observer import notificationAlertObserver
from abc import ABC, abstractmethod

class StockObservable(ABC):
    @abstractmethod
    def add(self, observer: notificationAlertObserver.NotificationAlertObserver):
        pass

    @abstractmethod
    def remove(self, observer: notificationAlertObserver.NotificationAlertObserver):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass

    @abstractmethod
    def setStockCount(self, newStocksAdded: int):
        pass

    @abstractmethod
    def getStocksCount(self):
        pass