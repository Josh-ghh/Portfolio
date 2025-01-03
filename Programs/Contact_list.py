list1 = []
dict = {}

def add():
    amount = int(input("how many contacts would you like to add? "))
    for i in range(amount):
        contact = input("enter a contact name")
        number = int(input("enter a phone number"))
        l_add = contact +str(number)
        
        dict.update({contact: number})
        list1.append(l_add)
    
    print(dict)
    print(list1)
    menu()

def remove():
    amount = int(input("how many contacts would you like to remove?"))
    for i in range(amount):
            c_remove = input("give me a name to remove")
            n_remove = int(input("give me a number to remove"))
            
            dict.pop(c_remove, n_remove)
            print(dict)
    menu()

def menu():
    menu = int(input(" 1. add 2. remove 3. exit"))
    if menu == 1:
        add()
    elif menu == 2:
        remove()
    else:
        print("Terminated")
        
menu()