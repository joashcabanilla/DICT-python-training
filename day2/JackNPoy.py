print("Jack N Poy Game")
print("[P/p] - Paper")
print("[R/r] - Rock")
print("[S/s] - Scissors")

p1 = str(input("Player 1: "))
p2 = str(input("Player 2: "))

if p1.lower() == "p" and p2.lower() == "r":
    print("Player 1 wins!\nPaper covers rock")
elif p2.lower() == "p" and p1.lower() == "r":
    print("Player 2 wins!\nPaper covers rock")
elif p1.lower() == "p" and p2.lower() == "s":
    print("Player 2 wins!\nScissors cut paper")
elif p2.lower() == "p" and p1.lower() == "s":
    print("Player 1 wins!\nScissors cut paper")
elif p1.lower() == "r" and p2.lower() == "s":
    print("Player 1 wins!\nRock breaks scissors")
elif p2.lower() == "r" and p1.lower() == "s":
    print("Player 2 wins!\nRock breaks scissors")
elif p1.lower() == "p" and p2.lower() == "p":
    print("Draw")
elif p1.lower() == "r" and p2.lower() == "r":
    print("Draw")
elif p1.lower() == "s" and p2.lower() == "s":
    print("Draw")
elif (p1.upper() != "R" or p1.upper() != "P" or p1.upper() != "S") and \
        (p2.upper() == "R" or p2.upper() == "P" or p2.upper() == "S"):
    print(f"Invalid input for Player 1: {p1}")
elif (p2.upper() != "R" or p2.upper() != "P" or p2.upper() != "S") and \
        (p1.upper() == "R" or p1.upper() == "P" or p1.upper() == "S"):
    print(f"Invalid input for Player 2: {p2}")
else:
    print(f"Invalid input for Player 1: {p1}")
    print(f"Invalid input for Player 2: {p2}")
