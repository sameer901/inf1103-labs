import ast


def get_valid_input():
      stock = input("enter Stock Value or enter quit to exit: ")
      if stock == "quit":
            return "quit"
      
      elif stock.startswith("-") and stock[1:].isdigit() :
            print("Invalid input, enter a valid integer")
            return "rejected"

      elif stock.isdigit() == False:
            print("Invalid input, enter a valid integer")
            return "rejected"
      else:
             stock = int(stock)
             return stock

      
def process_delivery(current_total, new_value):
      new_total = current_total + new_value  
      return new_total           

def calculate_tax(amount):
      tax_amount = amount * 0.10
      return tax_amount


def generate_report(total_units,failed_attempts):
        print("Total Deliveries Proccessed: " + str(total_units))
        print("Number of Failed/Rejected Entries: " + str(failed_attempts))


def load_inventory():
    try:
      file = open("inventory.txt", "r")
      data = file.read()
      data = data.split("\n")
      inventory = int(data[0])
      transaction_history = ast.literal_eval(data[1])

    except FileNotFoundError:
      inventory = 0
      transaction_history = []

    return inventory, transaction_history

def save_inventory(inventory,transaction_history):
   file = open("inventory.txt", "w")
   file.write(str(inventory))
   file.write("\n")
   file.write(str(transaction_history))
   file.close()


      
inventory, transaction_history = load_inventory()
failed_attempts = 0
deliveries_processed = 0
print("Current Inventory:", inventory)
print("Current Transaction History:", transaction_history)
print("\n")

while True:
      stock = get_valid_input()
      if stock == "quit":
        save_inventory(inventory, transaction_history)
        generate_report(deliveries_processed,failed_attempts)
        break
      
      elif stock == "rejected":
            failed_attempts += 1
            continue
      else :
            inventory = process_delivery(inventory, stock)
            transaction_history.append(stock)
            tax = calculate_tax(stock)
            deliveries_processed += 1