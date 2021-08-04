from os import system
phonebook = dict()
ch = ""

while ch.upper() != "X":
    system('cls')
    print("Simple Phonebook")
    print("[A] - Add Data")
    print("[V] - View Data")
    print("[X] - Exit")
    ch = str(input("Enter choice: "))
    if ch.upper() == "A":
        system('cls')
        print("Add Data")
        key = str(input("Enter key: "))
        value = str(input("Enter value: "))
        phonebook[key] = value
        input("Press any key to continue...")
    elif ch.upper() == "V":
        system('cls')
        print("View Data")
        for data in phonebook:
            print(f"{data}: {phonebook[data]}")
        input("Press any key to continue...")
