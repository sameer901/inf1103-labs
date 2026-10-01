import ast

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

inventory, transaction_history = load_inventory()

print("Current inventory :" + str(inventory))
print("Current History:" + str(transaction_history))
