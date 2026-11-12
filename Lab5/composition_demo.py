from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order


supplier = Supplier("S003", "Tech Supplies", "orders@example.com")

laptop = PhysicalProduct(
    "P301", "Laptop", 1200.0, 5, 2.5, supplier
)
photo_editor = DigitalProduct(
    "P302", "Photo Editor", 19.99, 10, 850.0, supplier
)

order_a = Order("O001")
order_b = Order("O002")

order_a.add_order_line(laptop, 2)
order_a.add_order_line(photo_editor, 1)
order_b.add_order_line(laptop, 1)

print("Order A line count:", len(order_a.order_lines))
print("Order B line count:", len(order_b.order_lines))
print(
    "Same laptop object:",
    order_a.order_lines[0].product is order_b.order_lines[0].product
)
print(
    "Same order line object:",
    order_a.order_lines[0] is order_b.order_lines[0]
)
print("Order A total:", order_a.calculate_total())
print("Order B total:", order_b.calculate_total())