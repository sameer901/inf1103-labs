from product import Product

#lab7
class DigitalProduct(Product):
    def __init__(  #Lab 8 , refactored the initializer to have type hint
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        download_size: float,
        supplier: Supplier
    ) -> None:
        super().__init__(product_id, name, price, stock, supplier)
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