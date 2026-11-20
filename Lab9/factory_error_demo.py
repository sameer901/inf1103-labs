from supplier import Supplier
from product_factory import ProductFactory


supplier = Supplier("S902", "Demo Supplier", "demo@example.com")

ProductFactory.create(
    "service",
    "S902",
    "Installation",
    30.0,
    5,
    supplier
)