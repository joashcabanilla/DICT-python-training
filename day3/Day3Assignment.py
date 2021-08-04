from os import system

bankWord = list()
answer = "Y"
while answer.upper() == "Y":
    system('cls')
    print("WORD BANK PROGRAM")
    word = str(input("Enter a word: "))
    bankWord.append(word)
    answer = str(input("Do you want to try again? input [Y/y] if yes and [N/n] if No: "))
    if answer.upper() == "N":
        system('cls')
        print("WORD BANK PROGRAM")
        print(f"Total Number of Words : {len(bankWord)}")
        print("List of Words:")
        for data in bankWord:
            print(f"-{data}")