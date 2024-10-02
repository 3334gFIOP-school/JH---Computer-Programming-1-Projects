# Jackson Hauley - Shopping List Manager

# Initializing List
ShoppingList = []

# Functions
def AddToList(add):
    ShoppingList.append(add)
    
def RemoveFromList(item):
    ShoppingList.remove(item)

def ask():
    print("\nShopping List Manager")
    print("1. Add an Item\n2. Remove an Item\n3. Review List\n4. Leave List Manager")
    selection = int(input('Which one do you want to do?: '))
    if selection == 1:
        adding = input("What item do you want to add to your list?: ")
        AddToList(adding)
        print("Added",adding,"to the list!")
        ask()
    elif selection == 2:
        remove = input("What is the item you want to remove?: ")
        if remove in ShoppingList:
            RemoveFromList(remove)
            print("Successfully removed",remove,"from the list!")
            ask()
        else:
            print("Item not in list!")
            ask()
    elif selection == 3:
        print("Here is your shopping list!\n",ShoppingList)
        ask()
    elif selection == 4:
        print("Have a nice day!")
        print("Your final shopping list:",ShoppingList)


# Starting
ask()
    