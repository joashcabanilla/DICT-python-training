import random

fname = ["John", "Ryan", "Paul", "Princess", "Joy"]
mname = ["Jelay", "Ain", "Mark", "Santos", "Camuen"]
lname = ["Alcantara", "Juntado", "Robles", "Cureg", "Caisip"]
listname = list()

def name_gen(num):
        gen_fname = fname[num]
        gen_mname = mname[num]
        gen_lname = lname[num]
        generatedname = gen_fname + " " + gen_mname + " " + gen_lname
        return generatedname

ch = ""

while ch.upper() != "N":
    ch = str(input("Do you want to generate new name? [y/n] "))
    if ch.upper() == "Y":
        num = random.randint(0, 4)
        name = name_gen(num)
        listname.append(name)
        print(f"Your new name is {name}\n")
    elif ch.upper() == "N":
        print("Thank You!")
        print("List of names generated:")
        for n in listname:
            print(f"-{n}")