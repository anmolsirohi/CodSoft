import random

def get_user_choice():
    print("\nYour options: rock, paper, scissors")
    choice = input("What do you choose? ").strip().lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Oops! Invalid input. Please type rock, paper, or scissors.")
        choice = input("Try again: ").strip().lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)

    if winner == "tie":
        print("It's a tie! ")
    elif winner == "user":
        print("You win this round! ")
    else:
        print("Computer wins this round.")

    return winner

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    user_score = 0
    computer_score = 0
    round_num = 1

    while True:
        print(f"\n--- Round {round_num} ---")
        result = play_round()

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")

        again = input("\nWanna play again? (yes/no): ").strip().lower()
        while again not in ['yes', 'no']:
            again = input("Please type 'yes' or 'no': ").strip().lower()

        if again == 'no':
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print(" You're the champion!")
            elif user_score < computer_score:
                print(" Better luck next time!")
            else:
                print("It was a great match, a perfect tie!")
            break

        round_num += 1

# Start the game
if __name__ == "__main__":
    play_game()