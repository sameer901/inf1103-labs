from product import Product #lab7
from can_be_shipped import CanBeShipped #need can_be_shipped.py

#lab7
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
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
