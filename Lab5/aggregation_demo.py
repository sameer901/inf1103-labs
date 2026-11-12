from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory


supplier = Supplier("S002", "Office Supplies", "orders@example.com")
product = PhysicalProduct(
    "P201", "Monitor", 250.0, 8, 4.5, supplier
)

inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(product)
removed_product = inventory_a.remove_product("P201")

print("Found in Inventory A:", inventory_a.find_product("P201"))

if removed_product is not None:
    print("Removed product details:")
    removed_product.display_information()

    inventory_b.add_product(removed_product)
    print("Same object in Inventory B:",
          inventory_b.find_product("P201") is product)