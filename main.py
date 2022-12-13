from os import system as terminal

def room():
    while True:
        terminal("cls")
        print("Room Menu")
        print("1: Add")
        print("2: Modify")
        print("3: Delete")
        print("4: Return")

        choice = int(input("Choice: "))
        if choice == 1:
            #radd()
            pass
        if choice == 2:
            #rmodify()
            pass
        if choice == 3:
            #rdelete()
            pass
        if choice == 4:
            return


#Main Loop
while True:
    terminal("cls")
    print("Main Menu")
    print("1: Room")
    print("2: Customer")
    print("3: Bill")
    print("4: Exit")
    
    choice = int(input("Choice: "))
    if choice == 1:
        room()
    elif choice == 2:
        #customer()
        pass
    elif choice == 3:
        #bill()
        pass
    else:
        break