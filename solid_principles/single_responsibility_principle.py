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


class InvoiceDao:
    def __init__(self, invoice) -> None:
        self.invoice = invoice

    def save_to_db(self) -> None:
        print("logic to save to DB")


class InvoicePrinter:
    def __init__(self, invoice) -> None:
        self.invoice = invoice

    def print(self) -> None:
        print("printing invoice")


#Now All above these classes have single reason to change
