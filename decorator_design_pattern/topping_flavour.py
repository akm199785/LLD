from base_pizza import BasePizza

class Topping(BasePizza):
    pass

class ExtraCheese(Topping):

    def __init__(self, base_pizza:BasePizza) -> None:
        """constructor injection"""
        self.__base_pizza = base_pizza

    def cost(self) -> float:
        return self.__base_pizza.cost() + 15


class Mushroom(Topping):
    def __init__(self, base_pizza:BasePizza) -> None:
        """constructor injection"""
        self.__base_pizza = base_pizza

    def cost(self) -> float:
        return self.__base_pizza.cost() + 20

class Capsicum(Topping):
    def __init__(self, base_pizza:BasePizza) -> None:
        """constructor injection"""
        self.__base_pizza = base_pizza

    def cost(self) -> float:
        return self.__base_pizza.cost() + 30

