import random
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    if player_choice == "stone":
        if computer_choice == "scissor":
            return "You win! Stone stone scissor."
        else:
            return "You lose! Paper covers stone."

    elif player_choice == "paper":
        if computer_choice == "stone":
            return "You win! Paper covers stone."
        else:
            return "You lose! Scissor cut paper."

    elif player_choice == "scissor":
        if computer_choice == "paper":
            return "You win! Scissor cut paper."
        else:
            return "You lose! Stone beat scissor."
def main():
    choices = ["stone", "paper", "scissor"]

    print("Welcome to Stone, Paper, Scissor!")
    print("Available choices: stone, paper, scissor")

    while True:
        player_choice = input("Enter your choice: ").lower()

        if player_choice not in choices:
            print("Invalid option! Please choose again.")
            continue

        computer_choice = random.choice(choices)
        print("Computer chooses:", computer_choice)

        result = determine_winner(player_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

main()
