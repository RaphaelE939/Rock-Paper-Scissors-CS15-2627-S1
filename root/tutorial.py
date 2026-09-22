import random

def get_cpu_choice():
    choices = ["rock", "paper", "scissors"]
    cpu_choice = random.choice(choices)
    return cpu_choice

def get_player_choice():
    while True:
        player_choice = input("Rock, Paper or Scissors? ").strip().lower()
        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice
        else:
            print("Invalid input. Try again.")

def check_winner(cpu_choice, player_choice):
    if player_choice == cpu_choice:
        return "Tie"

    elif cpu_choice == "rock":
        if player_choice == "paper":
            return "Player"
        else:
            return "CPU"

    elif cpu_choice == "paper":
        if player_choice == "scissors":
            return "Player"
        else:
            return "CPU"

    elif cpu_choice == "scissors":
        if player_choice == "rock":
            return "Player"
        else:
            return "CPU"

    return None

cpu_choice = get_cpu_choice()
player_choice = get_player_choice()
winner = check_winner(cpu_choice, player_choice)

print(f"CPU chose: {cpu_choice}")
print(f"You chose: {player_choice}")
print(f"Winner: {winner}")