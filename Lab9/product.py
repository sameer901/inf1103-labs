from abc import ABC, abstractmethod #lab7
from supplier import Supplier

class Product(ABC): #Lab 8 , refactored the initializer to have type hint
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        supplier: Supplier
    ) -> None:
        price_value = float(price)
        stock_value = int(stock)

        if price_value <= 0:
            raise ValueError("Price must be greater than zero.")

        if stock_value < 0:
            raise ValueError("Stock cannot be negative.")
        
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price_value
        self.__stock: int = stock_value
        self.__supplier: Supplier = supplier

    def display_supplier_information(self) -> None: # Lab 8
        self.__supplier.display_information()

    def update_stock(self, quantity: int) -> None:
        quantity_value = int(quantity)

        if quantity_value < 0:
            raise ValueError("Stock cannot be negative.")

        self.__stock = quantity_value

    def display_information(self) -> None:
        print(f"ID:    {self.__product_id}")
        print(f"Name:  {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    def get_product_id(self) -> str:
        return self.__product_id

    def to_dict(self) -> dict[str, str | float | int | dict[str, str]]:
        return {
            "ID": self.__product_id,
            "Name": self.__name,
            "Price": self.__price,
            "Stock": self.__stock,
            "Supplier": self.__supplier.to_dict()
        }
    @abstractmethod
    def get_fulfilment_info(self)-> str: #lab7
        pass 

    def get_price(self) -> float:
        return self.__price   




