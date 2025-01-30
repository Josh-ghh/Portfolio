balance = 0


def add(balance):
    try:
        amount = float(input("Enter the amount of money you want to add "))
        balance = balance + amount
        print(balance)
    except ValueError:
        print("invalid response")


def show_balance(balance):
    if len(balance) == 0:
        print("Your bank account is empty.")
    else:
        print(f"Your balance is" {balance})


def withdraw(balance):
    try:
        amount = float(input("How much do you want to withdraw "))
        if amount > balance:
            print("You do not have enough funds to remove ")
            amount = float(input("How much do you want to withdraw "))
        else:
            balance =  balance - amount
            print(f"Your balance is" {balance})
    except ValueError:
        print("invalid response, exiting list removal")

def menu():
     while True:
        try:
            pick = int(input("Pick a number for what you'd like to do. 1. Show your Balance, 2. add to your bank account, 3. withdraw money, 4. exit"))
            if pick == 1:
                show_balance(balance)
            elif pick == 2:
                add(balance)
            elif pick == 3:
                withdraw(balance)
            elif pick == 4:
                print("exiting")
                break
            else:
                print("Invalid option. Please choose 1, 2, 3 or 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the menu option.")


menu()
