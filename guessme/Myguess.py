import random


def guess(x):
    random_number= random.randint(1, x)
    guess=0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 to {x}: "))
        if guess < random_number:
            print(f"Sorry Guess again. {guess} Too low ")
        elif guess > random_number:
            print(f"Sorry Guess again. {guess} Too high")

    print(f"Yay, Congrats. You have guessed the number {random_number}")
                    
guess(100)