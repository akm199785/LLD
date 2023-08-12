#Statement: classes should open for extension but close for modifications

class InvoiceDao:
    def __init__(self, invoice) -> None:
        self.invoice = invoice

    def save_to_db(self) -> None:
        print("logic to save to DB")


#suppose we need to save invoice into also as above class till now supporting 
#have only one method save_to_db so we should not modify it like adding another mother
#save_to_file also rather we should design such way that modification wont be needed anymore

# as following lets design that adhere L-principle

from abc import ABC, abstractmethod
#create interface like class in python
class InvoiceDao(ABC):
    @abstractmethod
    def save(self) -> None:
        raise NotImplementedError


class DatabaseInvoiceDao(InvoiceDao):
    def __init__(self, invoice) -> None:
        self.invoice = invoice

    #override base class method
    def save(self) -> None:
        print("logic for saving invoice into DB")

class FileInvoiceDao(InvoiceDao):
    def __init__(self, invoice) -> None:
        self.invoice = invoice

    #override base class method
    def save(self) -> None:
        print("logic for saving invoice into File")

#Now if we need to save invoice in another places we can just create another class
# and can achieve new saving mechanism without modifying current classes

