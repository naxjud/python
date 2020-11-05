import random

guess_number = 0
guess_count = 3
new_game = "y"

while new_game == "y":
    secret_number = random.randrange(1, 10)

    print("I am hiding a number between 1 and 10 can you guess it?")
    while guess_number < guess_count:
        guess = int(input(f"Guess nr. {guess_number+1}: "))
        guess_number += 1
        if guess == secret_number:
            print("You win!")
            guess_number = 0
            break
    else:
        print("Sorry you failed!")

    new_game = input("Play again? (y)es n(o) ")
    guess_number = 0

print("good bye thanks for playing")