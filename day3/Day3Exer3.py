# fruits = ["apple", "grapes", "kiwi", "banana", "avocado", "apple"]
#
# print("List of Fruits:")
# for f in fruits:
#     print(f)
#
# #append method
# fruits.append("orange")
# print("After appending......")
#
# print("List of Fruits:")
# for f in fruits:
#     print(f)
#
# #insert() method inserts an item at the specified location or index number
# fruits.insert(0,"guava")
#
# print("List of Fruits:")
# for f in fruits:
#     print(f)


#WORD BANK PROGRAM
from os import system
word = list()
ch = ""
while ch.upper() != "X":
    system('cls')
    print("WORD BANK PROGRAM")
    print("[A] - Add Word")
    print("[D] - Display")
    print("[E] - Edit")
    print("[R] - Remove")
    print("[X] - Exit")
    ch = str(input("Enter choice: "))
    if ch.upper() == "A":
        system('cls')
        print("Add a new word")
        w = str(input("Enter a word: "))
        word.append(w)
        input("Press any key to continue...")
    elif ch.upper() == "D":
        system('cls')
        print("Display all items")
        for w in word:
            print(f"- {w}")
        input("Press any key to continue...")
    elif ch.upper() == "E":
        system('cls')
        print("Update")
        i = 0
        found = False
        w = str(input("Enter word you want to edit: "))
        for wr in word:
            if wr == w:
                loc = i
            i += 1
        if found == True:
            newWord = str(input("Enter new word: "))
            word[loc] = newWord
        else:
            print("The word entered is not found in the list")
        input("Press any key to continue...")
    elif ch.upper() == "R":
        system('cls')
        print("Remove")
        wr = str(input("Enter word you want to remove:"))
        word.remove(wr)
        #word.pop(index number) remove item in list using index number
        input("Press any key to continue...")
    elif ch.upper() == "X":
        print("Thank You!")
