####################################
# Implement Your own Data Structures
####################################

# Much more user friendly ui has been added. 
# There still needs to be more error-handling such as if an incorrect name was provided but I am "content" with what is presented here. 
# Implementation of the bonus is included inside of viewing your inventory.

inventory = {}
user_input = 0

print("Welcome to the Inventory Manager!")
# While the user does not input '4' (which ends the program), it will continue asking the user which of these tabs does it want to access
while user_input != 4:
    print("1. View Inventory\n2. Add a new item\n3. Edit Inventory\n4. Exit\nPlease select an option: ", end="")
    user_input = int(input())

#If the user presses 1, it will show the entire inventory and calculate the price of everything in the inventory
    if user_input == 1:
        total_value = 0
        for key, value in inventory.items():
            item_total = value[0] * value[1]
            total_value += item_total
            print(f"Item: {key}, Quantity: {value[0]}, Price: ${value[1]}")
        print(f"Total value of all inventory: ${total_value:.2f}")

#If the user presses 2, the user will create a new inventory item with the program asking for the item name, quantity, and price in succession
    elif user_input == 2:
        inventory_item = input("Please provide the item name: ")
        item_quantity = int(input("Please provide the quantity: "))
        item_price = float(input("Please provide the price: "))
        inventory[inventory_item] = item_information = (item_quantity, item_price)

#If the user presses 3, the user is given the option to remove or update an item of their choice
    elif user_input == 3:
        remove_update = int(input("Would you like to REMOVE or UPDATE an item (1 or 2)? "))

#If the user wants to remove an item, it will print the inventory and prompt the user to provide the item name. If the user types 'EXIT', the user will be taken back to the main screen 
        if remove_update == 1:
            print(inventory)
            itemToRemove = input("Please provide the name of the item you would like to remove or type EXIT to return. ")
            if itemToRemove == "EXIT":
                continue
            del inventory[itemToRemove]

#If the user wants to update an item, it will prompt the user to provide the item name, then ask to provide a new quantity and price
        elif remove_update == 2:
            print(inventory)
            itemToUpdate = input("Please provide the name of the item you would like to update or type EXIT to return. ")
            if itemToUpdate == "EXIT":
                continue
            
            if itemToUpdate in inventory:
                new_quantity = int(input("Please provide a new quantity: "))
                new_price = float(input("Please provide a new price: "))
                inventory[itemToUpdate] = (new_quantity, new_price)
                print(f"{itemToUpdate} has been updated.")

#If the user wants to leave the program, they can press '4' and the program will shutdown
    elif user_input == 4:
        print("Exiting...")
        break