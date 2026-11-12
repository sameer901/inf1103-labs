from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


supplier = Supplier("S004", "Demo Supplier", "demo@example.com")

physical = PhysicalProduct(
    "P401", "Desk", 150.0, 5, 12.0, supplier
)
digital = DigitalProduct(
    "P402", "Drawing App", 29.99, 20, 500.0, supplier
)

show_product_details(physical)
show_product_details(digital)

inventory = Inventory()
inventory.add_product(physical)
inventory.add_product(digital)
inventory.display_all()