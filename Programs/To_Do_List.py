td_list = [ ] 

def list_add(td_list):
    try:
        amount = int(input("How many items do you want to add to the list?  "))
        for x in range(amount):
            add = input("Add to the to do list: ")
            td_list.append(add)
            print(td_list)
    except ValueError:
        print("invalid response, exiting list adding")

def show_list(td_list):
     if len(td_list) == 0:
        print("The shopping list is empty.")
     else:
        print(td_list)


def remove_list(td_list):
    try:
        amount = int(input("How many objectives do you want to remove from the list?  "))
        for x in range(amount):
            remove = input(" Enter an objective to remove")
            td_list.pop(remove)
            print(td_list)
    except ValueError:
        print("invalid response, exiting list removal")


def menu():
     z = True
     while z == True:
        try:
            pick = int(input("Pick a number for what you'd like to do. 1. Show the list, 2. add to the list, 3. remove an objective, 4. exit"))
            if pick == 1:
                show_list(td_list)
            elif pick == 2:
                list_add(td_list)
            elif pick == 3:
                remove_list(td_list)
            elif pick == 4:
                z = False
                print("exiting")
            else:
                print("Invalid option. Please choose 1, 2, 3 or 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the menu option.")


















