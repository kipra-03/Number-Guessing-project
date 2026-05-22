import random

print("=== NUMBER GUESSING GAME ===")

while True:

    print("\nSelect Difficulty Level")
    print("1. Easy (1 to 50)")
    print("2. Medium (1 to 100)")
    print("3. Hard (1 to 200)")

    level = input("Enter choice (1/2/3): ")

    if level == "1":
        max_number = 50

    elif level == "2":
        max_number = 100

    elif level == "3":
        max_number = 200

    else:
        print("Invalid choice!")
        continue

    secret_number = random.randint(1, max_number)

    attempts = 0

    print(f"\nI have selected a number between 1 and {max_number}")

    while True:

        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"\nCorrect! You guessed it in {attempts} attempts.")
            break

        elif guess > secret_number:
            print("Too high!")

        else:
            print("Too low!")

    play_again = input("\nDo you want to play again? (yes/no): ")

    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break