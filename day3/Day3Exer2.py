from os import system

balance = 10000
ch = ""
while ch.upper() != "X":
    system('cls') # clearing the console or clearscreen function
    print("ATM Program")
    print("[C] - Check Balance")
    print("[W] - Withdraw")
    print("[D] - Deposit")
    print("[X] - Exit")
    ch = str(input("Enter your choice: "))

    if ch.upper() == "C":
        system('cls')
        print("Balance Inquiry")
        print(f"Current Balance: {balance}")
        input("Press any key to continue...")  # it used as delay
    elif ch.upper() == "W":
        system('cls')
        print("Withdraw")
        amount = int(input("Enter amount: "))
        if amount > 0:
            if amount%100 == 0:
                 if amount < (balance-500):
                    balance = balance - amount
                 else:
                     print("Invalid amount. Insufficient funds.")
            else:
                print("Invalid amount. It should be in multiples of 100")
        else:
            print("Invalid amount. Amount should be greater than 0")
        input("Press any key to continue...")  # it used as delay
    elif ch.upper() == "D":
        system('cls')
        print("Deposit")
        amount = int(input("Enter amount: "))
        if amount > 0:
            balance = balance + amount
        else:
            print("Invalid amount. You should input positive amount")
        input("Press any key to continue...")  # it used as delay
    elif ch.upper() == "X":
        print("Thank you. The program will exit...")