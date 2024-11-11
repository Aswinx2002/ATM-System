import random
import sys

# Dictionary to store account information {account_number: [account_name, balance]}
acc_storage = {}


def deposit_acc():
    try:
        acc_number = int(input("Enter the Account Number:"))
        deposit = int(input("Enter the deposit amount:"))

        if deposit <= 0:
            print("Deposit amount must be greater than zero.")
            return

        if acc_number in acc_storage:
            balance = acc_storage[acc_number][1]
            balance += deposit
            acc_storage[acc_number][1] = balance
            print(f"Deposit successful. Current Balance: {balance}")
        else:
            print("Account is not found")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


def withdraw():
    try:
        acc_number = int(input("Enter the Account Number:"))
        withdraw_amount = int(input("Enter the withdraw amount:"))

        if withdraw_amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        if acc_number in acc_storage:
            balance = acc_storage[acc_number][1]
            if balance >= withdraw_amount:
                balance -= withdraw_amount
                acc_storage[acc_number][1] = balance
                print(f"Withdrawal successful. Current Balance: {balance}")
            else:
                print("Insufficient Balance")
        else:
            print("Account is not found")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


def check_bal():
    try:
        acc_number = int(input("Enter the Account Number:"))
        if acc_number in acc_storage:
            print(f"\nAccount Name: {acc_storage[acc_number][0]}\nAccount Balance: {acc_storage[acc_number][1]}")
        else:
            print("Account is not found\n")
    except ValueError:
        print("Invalid input. Please enter a valid account number.")


def add_acc():
    try:
        acc_name = input("Enter the Account Name:").strip()
        if not acc_name:
            print("Account name cannot be empty.")
            return

        initial_bal = int(input("Enter the initial balance:"))

        if initial_bal < 0:
            print("Initial balance must be zero or greater.")
            return

        acc_number = random.randrange(10 ** 10, 10 ** 11)

        # Ensure the generated account number is unique
        while acc_number in acc_storage:
            acc_number = random.randrange(10 ** 10, 10 ** 11)

        acc_storage[acc_number] = [acc_name, initial_bal]
        print("Account has been Created Successfully")
        print("Account No:", acc_number)

    except ValueError:
        print("Invalid input. Please enter a valid number for initial balance.")


def main():
    while True:
        print("\n")
        print(" " * 20, "Welcome to ATM Application")
        print(" " * 26, "------------")
        print("\nWhat would you like to do?\n")
        print("1. Create User Account")
        print("2. Check Balance")
        print("3. Withdraw Money")
        print("4. Deposit Money")
        print("5. Exit")

        try:
            user_input = int(input("\nEnter your choice:"))
            match user_input:
                case 1:
                    add_acc()
                case 2:
                    check_bal()
                case 3:
                    withdraw()
                case 4:
                    deposit_acc()
                case 5:
                    print("Exiting ATM application. Goodbye!")
                    sys.exit()
                case _:
                    print("Wrong choice. Please choose an item from the menu\n")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu options.")


# Run the main program loop
main()
