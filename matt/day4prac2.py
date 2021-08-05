import random

print("Jack N Poy Game")
print("Legend:")
print("P/p - Paper")
print("R/r - Rock")
print("S/s - Scissors")

computer = ["P", "R", "S"]


def display(player, user, com, winner, result):
    if player == "Draw":
        print(f"Draw")
        print(f"Computer bet: {com.upper()}")
        print(f"{user.upper()} vs {com.upper()}")
        print(f"Winner: Draw")
    else:
        print(f"{player} wins!")
        print(result)
        print(f"Computer bet: {com.upper()}")
        print(f"{user.upper()} vs {com.upper()}")
        print(f"Winner: {winner.upper()}")


def user_vs_com(user, com):
    if user.upper() == "P" and com.upper() == "R":
        display("User",  user, com, user, "Paper covers rock")
    elif user.upper() == "S" and com.upper() == "P":
        display("User", user, com, user, "Scissors cut paper")
    elif user.upper() == "R" and com.upper() == "S":
        display("User", user, com, user, "Rock breaks scissors")
    elif com.upper() == "P" and user.upper() == "R":
        display("Computer",  user, com, com, "Paper covers rock")
    elif com.upper() == "S" and user.upper() == "P":
        display("Computer", user, com, com, "Scissors cut paper")
    elif com.upper() == "R" and user.upper() == "S":
        display("Computer", user, com, com, "Rock breaks scissors")
    elif user.upper() == "P" and com.upper() == "P":
        display("Draw", user, com, com, "")
    elif user.upper() == "R" and com.upper() == "R":
        display("Draw", user, com, com, "")
    elif user.upper() == "S" and com.upper() == "S":
        display("Draw", user, com, com, "")


user = str(input("\nUser Input: "))
user_vs_com(user, computer[random.randint(0, 2)])
