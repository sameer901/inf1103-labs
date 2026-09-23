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

      
inventory = 0
failed_attempts = 0
deliveries_processed = 0

while True:
      stock = get_valid_input()
      if stock == "quit":
        generate_report(deliveries_processed,failed_attempts)
        break
      
      elif stock == "rejected":
            failed_attempts += 1
            continue
      else :
            inventory = process_delivery(inventory, stock)
            tax = calculate_tax(stock)
            deliveries_processed += 1
           