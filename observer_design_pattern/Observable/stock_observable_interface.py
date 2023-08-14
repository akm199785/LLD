from abc import ABC, abstractmethod
#abstract class (Interface is not present in python as we have in other programming language like Java/C++)


class MobileStockNotification(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def add_subscriber(self, subscriber):
        pass

    @abstractmethod
    def remove_subscriber(self, subscriber):
        pass

    @abstractmethod
    def notify_subscribers(self):
        pass

    @abstractmethod
    def get_count(self):
        pass

    @abstractmethod
    def get_product_name(self):
        pass

