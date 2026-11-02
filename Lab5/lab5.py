import json 
from product import Product
from inventory import Inventory





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