#Statement : subclass should extend the capability of parent class, not narrow down
# If a class B is subtype of class A then object of class A should be able to replacable by object of class B
# without breaking the behaviour of the program

# means classes should design in such way that adhere Liskov substitution principle

#lets take a example that not adhere this principle
from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def fly(self) -> None:
        raise NotImplementedError

class Duck(Bird):
    def __init__(self) -> None:
        super().__init__()

    def fly(self) -> None:
        print("Duck is flying")

class Orstrich(Bird):
    def __init__(self) -> None:
        super().__init__()

    def fly(self) -> None:
        pass

# there is problem with Orstrich because Duck and Orstrich both are bird but
# Orstrich cant flying so can't have flying implementations for Orstrich class
# this is voilating behaviour of Bird (parent class) Orstrich class narrow down the behaviour
# this is not adhering the principle of Liskov substitution

# Lets break it and make good design
from abc import ABC, abstractmethod

class Bird:
    def __init__(self) -> None:
        pass

class FlyingBird(Bird):
    def __init__(self) -> None:
        super().__init__()

    def fly(self):
        pass

class Duck(FlyingBird):
    def __init__(self) -> None:
        super().__init__()

    def fly(self):
        print("Duck is flying")

class Orstrich(Bird):
    def __init__(self) -> None:
        super().__init__()

#Now we have separated Flying bird class so that Flying bird can extend FlyingBird as base class
# that have both FlyingBird and Bird class capabilities
# and Orstrich inherit only Bird class capability and now it wont need to implement fly method
