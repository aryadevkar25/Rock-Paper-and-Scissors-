import random

def get_user_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    print(winner(user_choice, computer_choice))

if __name__ == "__main__":
    play_game()
