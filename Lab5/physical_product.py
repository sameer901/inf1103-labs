from product import Product #lab7
from can_be_shipped import CanBeShipped #need can_be_shipped.py
from supplier import Supplier


class PhysicalProduct(Product, CanBeShipped):
    def __init__(              #Lab 8 , refactored the initializer to have type hint
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        weight: float,
        supplier: Supplier
    ) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = float(weight)

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        return self.__weight * 2.00

    def to_dict(self):
        product_data = super().to_dict()
        product_data["Type"] = "physical"
        product_data["Weight"] = self.__weight
        return product_data
