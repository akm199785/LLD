#statement: interface should be such way that client should not implement unnecessary
# function they dont need 
#lets take example to understand

from abc import ABC, abstractmethod

class RestaurantEmployee(ABC):
    @abstractmethod
    def wash_dishes():
        pass
    @abstractmethod
    def serve_customer():
        pass
    @abstractmethod
    def cook_food():
        pass

class Waiter(RestaurantEmployee):
    def __init__(self) -> None:
        pass
    def serve_customer(self):
        print("Waiter is serving to customer")

    def wash_dishes():
        pass

    def cook_food():
        pass

waiter = Waiter()
waiter.serve_customer()

#there is problem with RestaurantEmployee interface Waiter is restaurant employee but 
# wash_dishes and cook_food is not duty of waiter and RestaurantEmployee class enforing to implement that
# so RestaurantEmployee is not adhere of interface segmented principle
# lets break it

class WaiterInterface(ABC):
    @abstractmethod
    def serve_customer():
        pass

    @abstractmethod
    def take_order():
        pass

class ChefInterface(ABC):
    @abstractmethod
    def cook_food():
        pass


class WorkerInterface(ABC):
    @abstractmethod
    def wash_dishes():
        pass

#Now each interace is segmented and have specific method related to that

