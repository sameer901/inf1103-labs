inventory = 0
failed_entries = 0

while True :
    stock = input("enter Stock Value or enter quit to exit: ")
    if stock == "quit":
         print("You total inventory is " + str(inventory))
         print("Total number of failed entries are " + str(failed_entries))
         break
    elif stock.startswith("-") and stock[1:].isdigit() :
            print("This a negative number, please input a valid number")
            failed_entries += 1
            continue
    elif stock.isdigit() == False:
            print("Please input a valid Integer number")
            failed_entries += 1
            #print(failed_entries)
            continue
    
    else: 
        stock = int(stock)
        inventory += stock 
        if inventory > 500:
              print("Warning!! inventory is more than 500.")
              print("You total inventory is " + str(inventory))
              print("Total number of failed entries are " + str(failed_entries))
              break