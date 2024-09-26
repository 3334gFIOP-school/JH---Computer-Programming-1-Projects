# Jackson Hauley - Comments Proficiency

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount): # Adds money to your bank account 
        if amount > 0: # If you did 0 then it dosent add anything so its invalid
            self.balance += amount # Adds amount to your balance
            return True # Booleon Retruns
        return False

    def withdraw(self, amount): # Removes money from your bank account 
        if 0 < amount <= self.balance: # Checks to make sure you have enough
            self.balance -= amount # Subtracts the amount you want to withdraw
            return True # boolean returns
        return False

    def get_balance(self): # Gives you the account numbers current balance
        return self.balance 

def create_account(): # Creates an account, assigns it a number, and assigns it a balance
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance)

def main(): # This is the interface that asks you what you want to do
    accounts = {} # This is the account dictionary
    while True:
        print("\n1. Create Account") # These are the options for what you can choose to do
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ") # Select an option to do
        
        if choice == '1': # If you choose 1 you can make an account
            account = create_account() # Runs the make account function
            accounts[account.account_number] = account 
            print(f"Account {account.account_number} created successfully!") # Lists your account which is now in the dictionary
        
        elif choice in ['2', '3', '4']: # If you dont pick 1 or 5
            account_number = input("Enter account number: ") # Select which account you want to check, withdraw, or deposit with
            if account_number in accounts: # Checks if your account exists in the dictionary
                account = accounts[account_number] # Selects your account
                if choice == '2': # If you choose 2 to deposit
                    amount = float(input("Enter deposit amount: ")) 
                    if account.deposit(amount): 
                        print(f"Deposited ${amount:.2f} successfully!") # Deposits amount with 2 digits after the decimal
                    else:
                        print("Invalid deposit amount.") # You didn't type in a float
                elif choice == '3': # If you choose to withdraw
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount): # Makes sure you have enough money
                        print(f"Withdrawn ${amount:.2f} successfully!") # Withdraws amount with 2 digits after the decimal (for money)
                    else:
                        print("Invalid withdrawal amount or insufficient funds.") # You ran out of money or you put an invalid input in
                else:
                    print(f"Current balance: ${account.get_balance():.2f}") # Becaue earlier it sed if you do 2 3 or 4 so if you did 4 it just goes here, to check the balance
            else: # If your account number is invalid
                print("Account not found.")
        
        elif choice == '5': # If you want to exit
            print("Thank you for using our banking system. Goodbye!")
            break # Lets you exit the loop
        
        else: # If you didn't input a number 1-5
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() # Start the loop and run it at the beggening