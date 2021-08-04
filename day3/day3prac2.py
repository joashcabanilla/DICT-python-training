answer = "Y"
while answer.upper() == "Y":
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    if (num1 + num2) % 2 == 0:
        print("The sum of two integers is Even")
    else:
        print("The sum of two integers is Odd")
    print("______________________________________________________________")
    answer = str(input("Try Again? Input [Y/y] if Yes and [N/n] if No: "))
    print()
    if answer.upper() == "N":
        print("Thank You!")