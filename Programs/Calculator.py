
def add(total):
    amount = int(input("How many numbers would you like to add together? "))
    
    for i in range(amount):
        num1 = int(input("Input a number to add: "))
        total += num1
    print(f"The total is {total}.")
   
      
def subtract():
    amount = int(input("How many numbers would you like to subtract? "))
    if amount < 1:
        print("You must input more than one number.")
        
    else:
        total = int(input("Input the first number to start with: "))
        for i in range(1, amount):
            num1 = int(input("Input a number to subtract: "))
            total -= num1
        print(f"The result is {total}")
        menu()
        
    
def div():
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter another number"))
    total = num1/num2
    print(f"The result is {total}.")
    menu()


def multiply(total):
    amount = int(input("How many number would you like to multiply? "))
    if amount < 1:
        print("You must have more than one number")
        amount = int(input("How many number would you like to multiply? "))
    else:
        for i in range(amount):
            num1 = int(input("Enter a number: "))
            total *= num1
        print(f"The total is {total}.")
    menu()


def menu():
    total = 0
    calc = input("Would you like to 1. Add, 2. Subtract, 3. Divide, 4. Multiply, 5. Exit ")
    if calc == "1" or calc == "add":
        add(total)
    elif calc == "2" or calc == "subtract":
        subtract()
    elif calc == "3" or calc == "divide":
        div()
    elif calc == "4" or calc == "multiply":
        multiply(total)
    else:
        exit()

menu()