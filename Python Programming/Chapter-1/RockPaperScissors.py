import random

choices = ["rock", "paper", "scissors"]



while (True):
    cpuChoice = random.choice(choices)
    playerChoice = input("Enter your choice (rock, paper, scissors): ").lower()
    print("Rock, Paper, Scissors, Shoot!")
    print("You chose: ", playerChoice)
    print("CPU chose: ", cpuChoice)
    if playerChoice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
    elif playerChoice == cpuChoice:
        print("It's a tie!")

    elif (playerChoice == "rock" and cpuChoice == "scissors") or \
         (playerChoice == "paper" and cpuChoice == "rock") or \
         (playerChoice == "scissors" and cpuChoice == "paper"):
        print("You win!")
    else:
        print("CPU wins!")
    print("Play Again? (y/n)")
    playAgain = input().lower()
    if playAgain != "y":
        print("Happy to play again!")
        break

