import random
import utils
# import sleep to show output for some time period
from time import sleep
# import only system from os
from os import system

# loop until user types n
while True:
    system('clear')
    # user give the range
    number_range = int(input("In welchem Bereich willst du, dass wir spielen? von 1 bis ?: "))
    print(f"Ok! Suche dir eine Zahl zwischen 1 und {number_range} aus und merke sie dir gut:")

    ready = input("bist du fertig? (j)a (n)ein: ")

    while ready == 'n':
        sleep(2)
        print("...")
        sleep(2)
        ready = input("und jetzt bist du fertig? (j)a (n)ein: ")

    system('clear')
    print("Ok! ich versuche deine Zahl zu erraten")

    min_zahl = 1
    max_zahl = number_range

    while True:
        guess = max_zahl + min_zahl -1 / 2


    # computer chooses a number from the range
    secret_number = random.randrange(1, number_range)
    gefunden = False
    versuche = 0

    print(f"Ok! Ich habe eine Zahl zwischen 1 und {number_range} ausgewählt")
    print("versuche sie zu erraten. \n Viel Glück!")

    # loop until found
    while not gefunden:
        versuche += 1
        # user guess
        user_guess = int(input("> "))

        # computer gives feedback

        if user_guess > secret_number:
            print("Die gesuchte Zahl ist kleiner")
        elif user_guess < secret_number:
            print("Die gesuchte Zahl ist größer")
        else:
            print(f"Hurra! Meine Zahl war wirklich {secret_number} !")
            print(f"Du hast {versuche} Versuche gebraucht, um die Zahl zu finden.\n Herzlichen Glückwunsch!")
            break

    # new game yes or no
    new_game = input("Willst du das Ratespiel nochmal spielen? (j)a (n)ein : ")

    # no break
    if new_game == 'n':
        break

# print thanks for playing
print("Danke für das Spielen. Bis zum nächsten mal. \n Möge dein erratungsvermögen bei dir bleiben. Tschüss.")
