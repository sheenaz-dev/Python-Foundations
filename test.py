import random

def play_game():  # BUG 1: Something is missing at the end of this line!
    options = ["rock", "paper", "scissors"]
    
    # BUG 2: Look at the quotation marks. One of them is missing!
    print("--- 🎮 Welcome to the Python Battle Arena 🎮 ---")

    # BUG 3: A colon is missing here too.
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower()

        if user_choice == 'quit':
            break
        
        computer_choice = random.choice(options)
        
        # BUG 4: Can you see the missing closing parenthesis ')'?
        print(f"Computer chose: {computer_choice}")

    print("Thanks for playing!")

play_game()