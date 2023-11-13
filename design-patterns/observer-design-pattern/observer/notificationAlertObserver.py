from abc import ABC, abstractmethod

class NotificationAlertObserver(ABC):
    @abstractmethod
    def update(self):
        pass