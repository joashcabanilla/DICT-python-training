arr = []
try:
    file = open("data.txt", "r")
    for line in file:
        line = line.strip("\n")
        print(line.upper())
        arr = line.split(" ")
        print(f"Total number of words: {len(arr)}")
        print("----------------------------")
except FileNotFoundError:
    print("File not found")
