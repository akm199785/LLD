from .notification_interface import NotificationSubscriber
from Observable.stock_observable_interface import MobileStockNotification


class MobileNotificationSubscriber(NotificationSubscriber):
    def __init__(self, phone_number:int, subscribed_item:MobileStockNotification) -> None:
        self.subscribed_item = subscribed_item
        self.phone_number = phone_number

    def update(self):
        count = self.subscribed_item.get_count()
        name = self.subscribed_item.get_product_name()
        print(f"Text message sent on phone number {self.phone_number} and message is : Hurry up! {count} {name} are left")
