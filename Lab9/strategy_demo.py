from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount


supplier = Supplier("S901", "Demo Supplier", "demo@example.com")
product = PhysicalProduct("P901", "Test Product", 250.0, 1, 1.0, supplier)

order = Order("O901", BulkDiscount(200, 20))
order.add_order_line(product, 1)

print("Bulk discount total:", order.calculate_total())

order.set_discount(PercentageDiscount(10))
print("Percentage discount total:", order.calculate_total())