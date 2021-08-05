import random

firstName = ["Josh", "Ash", "John", "Juan", "Paul"]
middleName = ["Florentino", "Everly", "Eliana", "Elena", "Willow"]
lastName = ["Cabanilla", "Cullen", "Camuen", "Santiago", "Papilirin"]
generatedName = list()

def genName(rand1,rand2,rand3):
        fname = firstName[rand1]
        mname = middleName[rand2]
        lastname = lastName[rand3]
        name = fname + " " + mname + " " + lastname
        return name

answer = ""

while answer.upper() != "N":
    answer = str(input("Do you want to generate new name? [y/n] "))
    if answer.upper() == "Y":
        rand1 = random.randint(0, 4)
        rand2 = random.randint(0, 4)
        rand3 = random.randint(0, 4)
        name = genName(rand1, rand2, rand3)
        generatedName.append(name)
        print(f"Your new name is {name}\n")
    elif answer.upper() == "N":
        print("Thank You!")
        print("List of names generated:")
        for data in generatedName:
            print(f"-{data}")
    else:
        print("invalid input")