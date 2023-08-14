from abc import ABC , abstractmethod

class NotificationSubscriber(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def update(self):
        pass
