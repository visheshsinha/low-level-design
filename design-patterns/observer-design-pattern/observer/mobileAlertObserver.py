from observer import notificationAlertObserver
from observable import stocksObservable

class MobileAlertObserver(notificationAlertObserver.NotificationAlertObserver):
    def __init__(self, emailId: str, observable: stocksObservable.StockObservable) -> None:
        self.emailId = emailId
        self.observable = observable

    def update(self):
        self.sendEmail()

    def sendEmail(self):
        print(f'Sending App Alert to {self.emailId}, - Product Back in Stock')