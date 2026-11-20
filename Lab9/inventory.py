from product import Product
class Inventory: #Lab 6
    def __init__(self) -> None: #Lab 8 , add type hint
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None: 
        self.__products.append(product)  #Lab 8 , add type hint for method 

    def remove_product(self, product_id: str) -> Product | None: #Lab 8 , add type hint for method + new method
        for index, product in enumerate(self.__products):
            if product.get_product_id().upper() == product_id.upper():
                return self.__products.pop(index)
        return None

    def find_product(self, product_id: str) -> Product | None: #Lab 8 , add type hint for method + change method name
        for product in self.__products:
            if product.get_product_id().upper() == product_id.upper():
                return product
        return None

    def search_product(self, product_id: str) -> Product | None: #Lab 8 , this is for naming convention because my lab5.py calls search_product
        return self.find_product(product_id)
    
    def display_all(self) -> None: #Lab 8 , add type hint for method 
        if not self.__products:
            print("No products in inventory.")
            return

        for product in self.__products:
            product.display_information()

        #print(f"{'ID':<6} | {'Product Name':<15} | {'Price':<10} | {'Stock':<6}")
        #print("-" * 48)





    def get_products(self) -> list[Product]: #Lab 8 , add type hint for method 
        return self.__products.copy()