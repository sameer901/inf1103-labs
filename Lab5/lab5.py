import json 

def save_inventory(products_list):
    # save the inventory list p
    with open("Lab5/lab5.json", "w") as file:
        json.dump(products_list, file, indent=4)

def add_product(new_id, name, price, stock):
    try:
        with open("Lab5/lab5.json","r") as file:
                products = json.load(file)

        new_item = {
                    "ID": new_id,
                    "Name": name,
                    "Price": float(price),
                    "Stock": int(stock)
                }

        products.append(new_item)
        with open("Lab5/lab5.json","w") as file:
            json.dump(products, file, indent=4)
        print(f"Success: '{name}' added!")

    except FileNotFoundError:
        print("Error, file not found")


def update_stock(product_id, new_stock):
    with open("Lab5/lab5.json","r") as file:
        products = json.load(file)

    found = False #To Track if we actually find a product

    for item in products:
        if item["ID"].upper() == product_id.upper():
            item["Stock"] = int(new_stock)
            found = True
            break # out of the loop

    if found:
        with open("Lab5/lab5.json", "w") as file:
            json.dump(products, file, indent=4)
        print(f"Success: Stock for ID '{product_id}' updated to {new_stock}!")
    else:
        print(f"Error: Product ID '{product_id}' not found.")



def search_product(product_id):
    #Open the file in read mode
    with open("Lab5/lab5.json", "r") as file:
        products = json.load(file)

    for item in products:
        #print(f"DEBUG: Checking item: {item}")
        if item['ID'].upper() == product_id.upper():
            print("\n--- Product Found ---")
            print(f"ID:    {item['ID']}")
            print(f"Name:  {item['Name']}")
            print(f"Price: ${item['Price']:.2f}")
            print(f"Stock: {item['Stock']}")
            return 
        
    print(f"\nError: Product ID '{product_id}' not found.")         

def display_all():
    try:
        with open("Lab5/lab5.json","r") as file:
            products = json.load(file)
        print(f"{'ID':<6} | {'Product Name':<15} | {'Price':<10} | {'Stock':<6}")
        print("-" * 48)

        for item in products:
            print(f"{item['ID']:<6} | {item['Name']:<15} | ${item['Price']:<9.2f} | {item['Stock']:<6}")
    except FileNotFoundError:
        print("Error, file not found")

def main_menu():
    while True:
        print("\n===== INVENTORY MANAGEMENT =====")
        print("1. Display All Products")
        print("2. Add New Product")
        print("3. Update Product Stock")
        print("4. Search Product by ID")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("Enter your choice")

        if choice == "1":
            print("\n ----- Current Inventory---------")
            display_all()
        elif choice == "2":
            print("\n--- Add a New Product ---")
            # Get input from the user
            new_id = input("Enter Product ID (e.g., P004): ")
            name = input("Enter Product Name: ")
            price = input("Enter Product Price: ")
            stock = input("Enter Stock Quantity: ")            # Pass the inputs into your function
            add_product(new_id, name, price, stock)

        elif choice == "3":
            print("\n--- Update Product Stock ---")
            product_id = input("Enter the Product ID to update: ")
            new_stock = input("Enter the new stock level: ")
            update_stock(product_id, new_stock)

        elif choice == "4":
            print("\n--- Search Product by ID ---")
            product_id = input("Enter the Product ID to find: ")
            search_product(product_id)  
             
        elif choice == "5":
                    print("\nSaving Inventory")
                    save_inventory()
                    print("Inventory Saved to json file")



        elif choice == "6":
            print("Exiting program. Goodbye!")
            break  # This breaks the while loop and ends the script
            
        else:
            print("Invalid choice! Please enter a number between 1 and 3.")

main_menu()