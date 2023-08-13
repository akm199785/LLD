from base_pizza import *
from topping_flavour import *

if __name__ == '__main__':
    #Lets create : FarmHouse + ExtraCheese
    print(ExtraCheese(FarmHouse()).cost())
    #Lets create : FarmHouse + ExtraCheese + Mushroom + Capsicum
    print(Capsicum(Mushroom(ExtraCheese(FarmHouse()))).cost())
    #Lets create : VegLoaded + Mushroom + Capsicum + ExtraCheese
    print(ExtraCheese(Capsicum(Mushroom(VegLoaded()))).cost())