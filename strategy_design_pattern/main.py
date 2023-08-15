from __future__ import annotations
from abc import ABC , abstractmethod
from typing import List

class Context:
    """
    Context class define interface for client
    """

    def __init__(self, strategy:Strategy) -> None:
        """
        Context class accept strategy through constructor but also provide setter function
        to changes it at runtime
        """
        self._stretegy = strategy
    
    @property
    def strategy(self) -> Strategy:
        """context maintain the reference to one of strategy object 
            Context doesnt know concrete class of strategy . It should work with 
            all stretegy via strategy interface
        """
        return self._stretegy

    @strategy.setter
    def strategy(self, strategy:Strategy) -> None:
        """Context provide setter function to replace strategy at runtime"""
        self._stretegy = strategy

    def do_some_business_logic(self) -> None:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """
        print("Context: Sorting data using the strategy")
        result = self._stretegy.do_algorithm(['a', 'd', 'c', 'f', 'e'])
        print(",".join(result))

class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """
    @abstractmethod
    def do_algorithm(self, data:List):
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        """sort list asceding order"""
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.
    context = Context(ConcreteStrategyA())
    print("")
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()
    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()
