class Inventory: #Lab 6
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id().upper() == product_id.upper():
                return product
        return None
    
    def display_all(self):
        if not self.__products:
            print("No products in inventory.")
            return

        print(f"{'ID':<6} | {'Product Name':<15} | {'Price':<10} | {'Stock':<6}")
        print("-" * 48)

        for product in self.__products:
            product.display_information()
            print("-" * 48)



    def get_products(self):
        return self.__products.copy()