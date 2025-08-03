import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("🪨 📄 ✂️ Rock, Paper, Scissors Game")
    choices = ["rock", "paper", "scissors"]
    
    while True:
        user = input("Enter rock, paper, or scissors (or q to quit): ").lower()
        if user == 'q':
            print("Thanks for playing!")
            break
        if user not in choices:
            print("Invalid choice. Try again.")
            continue

        computer = get_computer_choice()
        print(f"Computer chose: {computer}")
        print(get_winner(user, computer))
        print()

if __name__ == "__main__":
    main()