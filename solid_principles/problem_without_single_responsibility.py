# statement:  A class should have only 1 reason to change

class Markar:
    def __init__(self, name, colour, year, price) -> None:
         self.name = name
         self.colour = colour
         self.year = year
         self.price = price

class Invoice:
    def __init__(self, marker, quantity) -> None:
        self.marker = marker
        self.quantity = quantity

    def calculate_total_price(self ) -> float:
        return self.marker.price * self.quantity

    def print_invoice(self) -> None:
        print("logic to print invoice")

    def save_to_db(self) -> None:
        print("logic to save to DB")


# Invoice Class is voilating single responsiblity principles because it has 3 reason to changes
# 1. suppose we added GST in calculate_total_price then this will change
# 2. If printing logic changes then we have to changes it also
# 3. we have to change it if save to db logic changed

# we have to break it down -> printing logic need to have in separate class and
# also same for Saving to DB class should be separate

    
          