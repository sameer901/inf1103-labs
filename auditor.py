inventory = 0
failed_entries = 0

while True :
    stock = input("enter Stock Value or enter quit to exit")
    if stock == "quit":
        break
    elif stock.startswith("-") and stock[1:].isdigit() :
            print("This a negative number, please input a valid number")
            failed_entries += 1
            continue
    elif stock.isdigit() == False:
            print("Plese input a valid Integer number")
            failed_entries += 1
            #print(failed_entries)
            continue
    
    else: 
        stock = int(stock)
        inventory += stock 
        print("You total inventory is " + str(inventory))


#while Stock_Qty == 0:
#    stock = input("Enter Stock Value or enter 'quit' to exit ")
#    if Stock_Qty == "quit":
#        break
#    elif :
    
#    elif int(stock) :
#        if stock < 0 :
#            print("Enter a positive Value")
#        else :
    #input("Enter Stock  Value") = Stock_Qty
    #p#rint