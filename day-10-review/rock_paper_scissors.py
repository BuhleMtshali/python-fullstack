import random

def play_game():
    player_wins = 0
    computer_wins = 0
    choices = ["rock", "paper", "scissors"]

    while True:
        # Get player input and convert to lowercase for consistent comparison
        player_choice = input("Enter a choice (rock, paper, scissors) or 'exit' to stop: ").lower()
        if player_choice == 'exit':
            print("Thanks for playing!")
            break
        
        if player_choice not in choices:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        # Get computer's random choice
        computer_choice = random.choice(choices)
        print(f"\nYou chose {player_choice}, computer chose {computer_choice}.")

        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
        
        print(f"Score: Player {player_wins} - Computer {computer_wins}\n")

if __name__ == "__main__":
    play_game()
