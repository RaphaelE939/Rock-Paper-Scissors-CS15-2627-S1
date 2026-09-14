import random
player_score = 0
cpu_score = 0
tie_score = 0
def get_cpu_choice():
    choices = ["rock", "paper", "scissors"]
    cpu_choice = random.choice(choices)
    return cpu_choice
print(f" Welcome to the RPS Tournament. This is the amount of points you have: {player_score}. This is the amount of points the computer has: {cpu_score}. Try to get 3 points before the computer does! ")

def get_player_choice():
    while True:
        player_choice = input("What is your choice: Rock, Paper or Scissors? ").strip().lower()
        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice
        else:
            print("Invalid input. Try again.")

def check_winner(cpu_choice, player_choice):
    if cpu_choice == player_choice:
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


def play_round():
    global player_score, cpu_score, tie_score

    cpu = get_cpu_choice()
    player = get_player_choice()
    winner = check_winner(cpu, player)

    print(f"CPU chose: {cpu}")
    print(f"You chose: {player}")
    print(f"Round winner: {winner}")

    if winner == "Player":
        player_score += 1
    elif winner == "CPU":
        cpu_score += 1
    elif winner == "Tie":
        tie_score += 1

    print(f"Player Score: {player_score}, Computer Score: {cpu_score}, Tie Score: {tie_score}")
    if player_score == 3 or cpu_score == 3:
        return
    if player_score > cpu_score:
        print("You are winning 👌👍")
    elif cpu_score > player_score:
        print("You are losing 😓😢")
    else:
        print("It's a tie so far 😐")
    # I don't want it to show this when the player has won or lost.


while True:
    play_round()
    if player_score == 3:
        print("Tournament over, Player Wins!!")
        break
    elif cpu_score == 3:
            print("Tournament over, Computer Wins.")
            break