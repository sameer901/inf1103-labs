import json 

class Product: #Lab 6
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)
    
    def update_stock(self, quantity):
        self.__stock = int(quantity)

    def display_information(self):
        print(f"ID:    {self.__product_id}")
        print(f"Name:  {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    def get_product_id(self):
        return self.__product_id

    def to_dict(self):
        return {
            "ID": self.__product_id,
            "Name": self.__name,
            "Price": self.__price,
            "Stock": self.__stock
        }

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


def save_inventory(product_list):
    with open("Lab5/lab5.json", "w") as file:
        json.dump([product.to_dict() for product in product_list], file, indent=4) #updated

def load_inventory():
    inventory = Inventory()

    try:
        with open("Lab5/lab5.json", "r") as file:
            products = json.load(file)

        for item in products:
            product = Product(
                item["ID"],
                item["Name"],
                item["Price"],
                item["Stock"]
            )
            inventory.add_product(product)

    except FileNotFoundError:
        print("Inventory file not found. Starting with an empty inventory.")

    return inventory



def main_menu(): #refactored the classes into main menu
    inventory = load_inventory()

    while True:
        print("\n===== INVENTORY MANAGEMENT =====")
        print("1. Display All Products")
        print("2. Add New Product")
        print("3. Update Product Stock")
        print("4. Search Product by ID")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            product_id = input("Enter Product ID (e.g., P004): ")
            name = input("Enter Product Name: ")
            price = input("Enter Product Price: ")
            stock = input("Enter Stock Quantity: ")

            product = Product(product_id, name, price, stock)
            inventory.add_product(product)
            print(f"Success: '{name}' added!")

        elif choice == "3":
            product_id = input("Enter the Product ID to update: ")
            product = inventory.search_product(product_id)

            if product is None:
                print(f"Error: Product ID '{product_id}' not found.")
            else:
                new_stock = input("Enter the new stock level: ")
                product.update_stock(new_stock)
                print(f"Stock for '{product_id}' updated.")

        elif choice == "4":
            product_id = input("Enter the Product ID to find: ")
            product = inventory.search_product(product_id)

            if product is None:
                print(f"Product ID '{product_id}' not found.")
            else:
                product.display_information()

        elif choice == "5":
            save_inventory(inventory.get_products())
            print("Inventory saved.")

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

main_menu()