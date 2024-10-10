# Jackson Hauley - What are these numbers

# Setup


# Defining Functions
def insert_commas(num):
    num = f"{num:,}"
    return num

def add_decimals(decimals,num):
    num = f"{num:.{decimals}f}"
    return num

def make_percentage(decimals,num):
    num = f"{num:.{decimals}%}"
    return num

def make_dollar(num):
    num = f"${num:,.2f}"
    return num

def start():
    print("\nNumber Format Converter\n================================")
    print("1. insert commas every 3 digits\n2. add an amount of decimals\n3. turn a number into a percentage\n4. turn a number into money format")
    try:
        selection = int(input("What action do you want to choose?(1-4): "))
    except ValueError:
        print("Invalid input!")
        start()
    if selection == 1:
        num = insert_commas(int(input("What number do you want to add commas too?: ")))
        print(f"\nYour number with commas added is {num}")
        start()
    elif selection == 2:
        num = add_decimals(int(input("How many decimal places do you want to go to?: ")),int(input("What number do you want to add those decimal places too?: ")))
        print(f"\nYour number with decimals added is {num}")
        start()
    elif selection == 3:
        num = make_percentage(int(input("How many decimal places do you want the percatages to go?: ")),int(input("What number do you want to make a percentage?: ")))
        print(f"\nYour number as a percantage is {num}")
        start()
    elif selection == 4:
        num = make_dollar(int(input("What number do you want to turn into money format?: ")))
        print(f"\nYour number in money format is {num}")
        start()
    else:
        print("\nInvalid input!")
        start()


# Startup
start()