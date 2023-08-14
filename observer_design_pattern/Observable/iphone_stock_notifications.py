from .stock_observable_interface import MobileStockNotification
from Observer.notification_interface import NotificationSubscriber

class IphoneStockNotification(MobileStockNotification):
    def __init__(self) -> None:
        self.subscribers = []
        self.__count = 0
        self.__product_name = "Iphone 14"

    def add_subscriber(self, subscriber:NotificationSubscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber:NotificationSubscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update()

    def add_count(self, count:int):
        if self.__count == 0:
            self.__count = count
            self.notify_subscribers()

    def get_count(self):
        return self.__count

    def get_product_name(self):
        return self.__product_name



