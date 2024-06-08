import random

def game():
    user_score = 0
    computer_score = 0
    choices = ["rock", "paper", "scissors"]

    while True:
        computer_choice = random.choice(choices)
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        print(f"\nUser choice: {user_choice}, Computer choice: {computer_choice}\n")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            user_score += 1
            print("You win this round!")
        else:
            computer_score += 1
            print("You lose this round.")

        print(f"Score: Player {user_score}, Computer {computer_score}\n")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Game Over.")
    print(f"Final Score: Player {user_score}, Computer {computer_score}")

game()