s_list=[ ]
def shop_add(s_list):
        try:
            amount = int(input("How many items do you want to add to the list?  "))

            for x in range(amount):
                add = input("Add to the shopping list: ")
                s_list.append(add)
                print(s_list)
        except ValueError:
            print("invalid response, exiting list adding")


def show_list(s_list):
    if len(s_list) == 0:
        print("The shopping list is empty.")
    else:
        print(s_list)

def remove_item(s_list):
    try:
        amount = int(input("How many items do you want to remove from the list?  "))
        for x in range(amount):
            remove = input(" enter an item to remove ")
            s_list.pop(remove)
            print(s_list)
    except ValueError:
        print("invalid response, exiting list removal")

def menu():
    
    while True:
        try:
            pick = int(input("Pick a number for what you'd like to do. 1. Show the list, 2. add to the list, 3. remove an item from the list, 4. exit"))
            if pick == 1:
                show_list(s_list)
            elif pick == 2:
                shop_add(s_list)
            elif pick == 3:
                    remove_item(s_list)
            elif pick == 4:
                print("exiting")
                break
            else:
                print("Invalid option. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the menu option.")



menu()
