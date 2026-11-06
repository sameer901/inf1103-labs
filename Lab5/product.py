from abc import ABC, abstractmethod #lab7

class Product(ABC): #Lab 6
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)
    
    def update_stock(self, quantity):
        self.__stock = int(quantity)

    def display_information(self):
        print(f"ID:    {self.__product_id}")
        print(f"Name:  {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    def get_product_id(self):
        return self.__product_id

    def to_dict(self):
        return {
            "ID": self.__product_id,
            "Name": self.__name,
            "Price": self.__price,
            "Stock": self.__stock
        }
    @abstractmethod
    def get_fulfilment_info(self): #lab7
        pass 

#lab7
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

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

#lab7
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = float(download_size)

    def display_information(self):
        super().display_information()
        print(f"Download size: {self.__download_size} MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally."

    def to_dict(self):
        product_data = super().to_dict()
        product_data["Type"] = "digital"
        product_data["DownloadSize"] = self.__download_size
        return product_data