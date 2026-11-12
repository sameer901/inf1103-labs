from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


supplier = Supplier("S005", "Demo Supplier", "demo@example.com")

physical = PhysicalProduct(
    "P501", "Camera", 400.0, 6, 0.8, supplier
)
digital = DigitalProduct(
    "P502", "Video Editor", 49.99, 15, 1200.0, supplier
)

inventory = Inventory()
inventory.add_product(physical)
inventory.add_product(digital)

for product in inventory.get_products():
    product.display_information()
    print(product.get_fulfilment_info())