from pathlib import Path
import sys
import unittest
import io
import tempfile
from contextlib import redirect_stdout
from unittest.mock import patch


# --------------python -m unittest discover -s Lab9/tests -p "test_*.py" -v #
#Use the command above to run the test file
# Add the Lab9 folder to Python's import path.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lab5 import get_positive_float, load_products
from bulk_discount import BulkDiscount
from digital_product import DigitalProduct
from no_discount import NoDiscount
from order import Order
from percentage_discount import PercentageDiscount
from physical_product import PhysicalProduct
from product_factory import ProductFactory
from supplier import Supplier
from inventory import Inventory


class Lab9Tests(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("SUP001", "Test Supplier", "test@example.com")
        self.product = PhysicalProduct(
            "P001", "Test Product", 100.0, 10, 2.0, self.supplier
        )

    def test_no_discount(self):
        self.assertEqual(NoDiscount().apply(250.0), 250.0)

    def test_percentage_discount(self):
        self.assertAlmostEqual(PercentageDiscount(10).apply(250.0), 225.0)

    def test_bulk_discount(self):
        self.assertEqual(BulkDiscount(200, 20).apply(250.0), 230.0)

    def test_order_uses_and_can_change_discount(self):
        order = Order("O001", BulkDiscount(200, 20))
        order.add_order_line(self.product, 2)
        self.assertEqual(order.calculate_total(), 180.0)

        order.set_discount(PercentageDiscount(10))
        self.assertAlmostEqual(order.calculate_total(), 180.0)

    def test_factory_creates_physical_product(self):
        product = ProductFactory.create(
            "physical", "P002", "Desk", 150.0, 5,
            self.supplier, weight=12.0
        )
        self.assertIsInstance(product, PhysicalProduct)

    def test_factory_creates_digital_product(self):
        product = ProductFactory.create(
            "digital", "D001", "Photo Editor", 20.0, 10,
            self.supplier, download_size=500.0
        )
        self.assertIsInstance(product, DigitalProduct)

    def test_factory_rejects_unknown_type(self):
        with self.assertRaisesRegex(ValueError, "Unknown product type"):
            ProductFactory.create(
                "service", "S001", "Installation", 30.0, 5, self.supplier
            )

    def test_product_rejects_nonpositive_price(self):
        with self.assertRaisesRegex(ValueError, "Price must be greater than zero"):
            PhysicalProduct("P003", "Bad Price", 0, 1, 1.0, self.supplier)

    def test_product_rejects_negative_stock(self):
        with self.assertRaisesRegex(ValueError, "Stock cannot be negative"):
            PhysicalProduct("P004", "Bad Stock", 10, -1, 1.0, self.supplier)

    def test_update_stock_rejects_negative_stock(self):
        with self.assertRaisesRegex(ValueError, "Stock cannot be negative"):
            self.product.update_stock(-1)

    def test_order_line_rejects_nonpositive_quantity(self):
        with self.assertRaisesRegex(ValueError, "Quantity must be greater than zero"):
            Order("O002").add_order_line(self.product, 0)

    def test_get_positive_float_retries_until_valid(self):
        output = io.StringIO()

        with patch("builtins.input", side_effect=["abc", "-5", "12.50"]):
            with redirect_stdout(output):
                result = get_positive_float("Enter price: ")

        self.assertEqual(result, 12.5)
        self.assertEqual(
            output.getvalue().splitlines(),
            [
                "Please enter a valid number, e.g. 12.50",
                "Please enter a number greater than zero."
            ]
        )

    def test_load_products_skips_bad_rows_and_loads_valid_rows(self):
        csv_content = (
            "product_type,product_id,name,price,stock_quantity\n"
            "physical,P101,Desk Lamp,25.00,10\n"
            "digital,D101,Photo Editor,49.90,100\n"
            "service,S101,Installation,30.00,5\n"
            "physical,P102,Office Chair,abc,3\n"
            "physical,P103,Monitor Stand,39.50,7\n"
        )

        with tempfile.TemporaryDirectory() as folder:
            csv_path = Path(folder) / "products.csv"
            csv_path.write_text(csv_content, encoding="utf-8")
            inventory = Inventory()
            output = io.StringIO()

            with redirect_stdout(output):
                load_products(str(csv_path), inventory, self.supplier)

        self.assertEqual(len(inventory.get_products()), 3)
        self.assertIn("Unknown product type: service", output.getvalue())
        self.assertIn("3 products loaded.", output.getvalue())
        self.assertIn("Load attempt finished.", output.getvalue())

    def test_load_products_handles_missing_file(self):
        with tempfile.TemporaryDirectory() as folder:
            missing_path = Path(folder) / "missing.csv"
            inventory = Inventory()
            output = io.StringIO()

            with redirect_stdout(output):
                load_products(str(missing_path), inventory, self.supplier)

        self.assertIn("Products file not found:", output.getvalue())
        self.assertIn("Load attempt finished.", output.getvalue())
        self.assertNotIn("products loaded.", output.getvalue())


if __name__ == "__main__":
    unittest.main()