import random

print("Jack N Poy Game")
print("Legend:")
print("P/p - Paper")
print("R/r - Rock")
print("S/s - Scissors\n")

legend = ["P", "R", "S"]


def display(player_winner, result, user_bet, com_bet, winner):
    print(f"{player_winner} wins!")
    print(result)
    print(f"Computer bet: {com_bet.upper()}")
    print(f"{user_bet.upper()} vs {com_bet.upper()}")
    print(f"Winner: {winner.upper()}")


def draw(user_bet, com_bet):
    print(f"Draw")
    print(f"Computer bet: {com_bet.upper()}")
    print(f"{user_bet.upper()} vs {com_bet.upper()}")
    print(f"Winner: Draw")


def user_vs_com(user_bet, com_bet):
    if user_bet.upper() == "P" and com_bet.upper() == "R":
        display("User", "Paper covers rock", user_bet, com_bet, user_bet)
    elif user_bet.upper() == "S" and com_bet.upper() == "P":
        display("User", "Scissors cut paper", user_bet, com_bet, user_bet)
    elif user_bet.upper() == "R" and com_bet.upper() == "S":
        display("User", "Rock breaks scissors", user_bet, com_bet, user_bet)
    elif com_bet.upper() == "P" and user_bet.upper() == "R":
        display("Computer", "Paper covers rock", user_bet, com_bet, com_bet)
    elif com_bet.upper() == "S" and user_bet.upper() == "P":
        display("Computer", "Scissors cut paper", user_bet, com_bet, com_bet)
    elif com_bet.upper() == "R" and user_bet.upper() == "S":
        display("Computer", "Rock breaks scissors", user_bet, com_bet, com_bet)
    elif user_bet.upper() == "P" and com_bet.upper() == "P":
        draw(user_bet, com_bet)
    elif user_bet.upper() == "R" and com_bet.upper() == "R":
        draw(user_bet, com_bet)
    elif user_bet.upper() == "S" and com_bet.upper() == "S":
        draw(user_bet, com_bet)
    else:
        print("Invalid Input for User")


user = str(input("User Input: "))
user_vs_com(user, legend[random.randint(0, 2)])
