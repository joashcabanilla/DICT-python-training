print("Record App")
print("[A] - Add")
print("[V] - View")
print("[X] - Exit")
ch = str(input("Enter choice: "))

while ch.upper() != "X":
    if ch.upper() == "A":
        try:
            file = open("data.txt", "a")
            name = str(input("Enter name: "))
            contact = str(input("Enter contact: "))
            file.write(name + "#" + contact + "\n")
            file.close()
        except FileNotFoundError:
            print("File does not exists")
    elif ch.upper() == "V":
        try:
            file = open("data.txt", "r")
            print("=========DATA===========")
            for line in file:
                line = line.strip("\n")
                arr = line.split("#")
                print(f"{arr[0]}\t\t{arr[1]} ")
            file.close()
        except FileNotFoundError:
            print("File does not exists")
