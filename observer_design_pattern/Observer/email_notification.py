from .notification_interface import NotificationSubscriber
from Observable.stock_observable_interface import MobileStockNotification


class EmailNotificationSubscriber(NotificationSubscriber):
    def __init__(self, email:str, subscribed_item: MobileStockNotification) -> None:
        self.email = email
        self.subscribed_item = subscribed_item

    def update(self):
        count = self.subscribed_item.get_count()
        name = self.subscribed_item.get_product_name()
        print(f"Email sent to {self.email} and message is : Hurry up! {count} {name} are left")


