from abc import ABC, abstractmethod

class BasePizza(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def cost(self) -> float:
        pass

class Margherita(BasePizza):
    def __init__(self) -> None:
        super().__init__()

    def cost(self) -> float:
        return 100

class FarmHouse(BasePizza):
    def __init__(self) -> None:
        super().__init__()

    def cost(self) -> float:
        return 450

class VegLoaded(BasePizza):
    def __init__(self) -> None:
        super().__init__()

    def cost(self) -> float:
        return 350

