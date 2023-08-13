#statement: classes should depend on interface rather than concreate classes

# The dependency inversion principle aims to reduce the coupling between classes by creating an abstraction layer between them.

#Lets take example to understand

class FXConverter:
    def __init__(self, from_currency, to_currency, amount) -> None:
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = amount
        self.conversion_rate = 1.2 # we will use api for get conversion rate

    def convert(self) -> float:
        return self.amount * self.conversion_rate

class App:
    def start(self) -> None:
        converter = FXConverter()
        converter.convert("EUR", "USD", 100)

# there problem with App class , it is directly depend on
# in future if F'X API changes then we need to changes App class also 
# then if we need to implement another type converter then we also need to change App class

# Lets break it down 


from abc import ABC, abstractmethod

class CurrencyConverter(ABC):
    @abstractmethod
    def convert()-> None:
        pass

class FXConverter(CurrencyConverter):
    def __init__(self, from_currency:str, to_currency:str, amount:float) -> None:
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = amount
        self.conversion_rate = 1.2
    
    def convert(self) -> None:
        converted_amount = self.amount * self.conversion_rate
        print("Converting currency using FX API")
        print(f"{self.amount} in {self.from_currency} is equal to {converted_amount} in {self.to_currency}")

class AlphaConverter(CurrencyConverter):
    def __init__(self, from_currency:str, to_currency:str, amount:float) -> None:
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = amount
        self.conversion_rate = 1.15
    
    def convert(self) -> None:
        converted_amount = self.amount * self.conversion_rate
        print("Converting currency using Alpha API")
        print(f"{self.amount} in {self.from_currency} is equal to {converted_amount} in {self.to_currency}")

class App:
    def __init__(self, converter:CurrencyConverter) -> None:
        self.converter = converter
    def start(self):
        self.converter.convert()


if __name__ == '__main__':
    App(FXConverter("EUR", "USD", 100)).start()
    App(AlphaConverter("EUR", "USD", 100)).start()

#Now this is decoupled and adhere dependency inversion principle

    
