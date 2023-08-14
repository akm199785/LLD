from Observable.iphone_stock_notifications import IphoneStockNotification
from Observer.email_notification import EmailNotificationSubscriber
from Observer.mobile_notification import MobileNotificationSubscriber

if __name__ == "__main__":
    iphoneStockNotification = IphoneStockNotification()
    #add two emails subscriber
    iphoneStockNotification.add_subscriber(EmailNotificationSubscriber("abc@gmail.com", iphoneStockNotification))
    iphoneStockNotification.add_subscriber(EmailNotificationSubscriber("bcd@gmail.com", iphoneStockNotification))
    #add two Mobile Subscriber
    iphoneStockNotification.add_subscriber(MobileNotificationSubscriber(9885782893, iphoneStockNotification))
    iphoneStockNotification.add_subscriber(MobileNotificationSubscriber(9384487832, iphoneStockNotification))
    iphoneStockNotification.add_count(10)


