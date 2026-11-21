# Dice Simulator

import random

while True:
    choice = input("Roll the dice? (yes/no): ")

    if choice.lower() == "yes":
        number = random.randint(1, 6)
        print("Dice Number:", number)

    elif choice.lower() == "no":
        print("Game ended")
        break

    else:
        print("Invalid choice")
