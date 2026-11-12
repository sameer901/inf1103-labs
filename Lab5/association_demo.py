from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


supplier = Supplier("S001", "Tech Supplies", "sales@example.com")

physical = PhysicalProduct(
    "P101", "Laptop", 1200.0, 15, 3.0, supplier
)
digital = DigitalProduct(
    "P102", "Photo Editor", 19.99, 10, 850.0, supplier
)

del supplier

physical.display_supplier_information()
digital.display_supplier_information()