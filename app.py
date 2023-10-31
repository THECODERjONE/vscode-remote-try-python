#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console
print("hello world")

import random

class Rock:
    def __init__(self):
        self.name = "rock"
        self.beats = "scissors"

class Paper:
    def __init__(self):
        self.name = "paper"
        self.beats = "rock"

class Scissors:
    def __init__(self):
        self.name = "scissors"
        self.beats = "paper"

elements = [Rock(), Paper(), Scissors()]
player_score = 0  # Initialize player's score
computer_score = 0  # Initialize computer's score

def player_input():
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    if player_choice in ["rock", "paper", "scissors"]:
        return player_choice
    else:
        print("Please choose one of the given options.")
        return player_input()

def determine_winner(player_choice, computer_choice):
    global player_score, computer_score  # Access the global score variables
    if player_choice == computer_choice.name:
        print("It's a tie!")
    elif player_choice == computer_choice.beats:
        print("You win!")
        player_score += 1  # Increment the player's score
    else:
        print("You lose!")
        computer_score += 1  # Increment the computer's score

def play_again():
    print("Player's score:", player_score)  # Display player's score
    print("Computer's score:", computer_score)  # Display computer's score
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        main()
    elif play_again == "no":
        print("Thanks for playing! Final scores - Player:", player_score, "Computer:", computer_score)
    else:
        print("Please choose yes or no.")
        play_again()

def main():
    global player_choice
    player_choice = player_input()
    computer_choice = random.choice(elements)
    print("The computer chose: " + computer_choice.name)
    determine_winner(player_choice, computer_choice)
    play_again()

main()
