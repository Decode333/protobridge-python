import random

choices = ["deer","bear","rat","lion","goat"]
choice = random.choice(choices)

counter=0
guessed = "_" * len(choice)
for i in range(7):

    print(f"Animal name: {guessed}")
    user_choice = input(f"Guess the animal name. {choices}. \n Enter one letter at a time: ")
    if user_choice.lower() in choice:
        pos = choice.index(user_choice.lower())
        guessed = guessed[:pos] + user_choice.lower() + guessed[pos+1:]
        print(f"Correct guess: {guessed}")
        if guessed == choice:
            print("You guessed the animal name correctly!")
            break
    else:
        print("Incorrect guess.")

    counter+=1

    if counter<7:
        print("Available attempts: ", 7-counter)
    elif counter==7:
        print("You have used all your attempts. The correct answer is: ", choice)


