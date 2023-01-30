import random

def get_choices():
    objects = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper, scissors) ")
    computer_choice = random.choice(objects)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!" 
    elif player == "rock" and computer == "scissors":
        return "Rock smashes scissors! You win!"
    



check_win("rock", "paper")


