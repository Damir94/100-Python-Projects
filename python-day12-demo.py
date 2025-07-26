
import art5, random

print(art5.logo)
print("Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100.")

user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

random_number = random.randrange(1, 101)

if user_choice == "easy":
    guess_attempts = 10
    should_continue_guessing = True

    while should_continue_guessing:
        print(f"You have {guess_attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        if user_guess == random_number:
            print(f"You got it! The answer was {user_guess}.")
            should_continue_guessing = False
        elif user_guess > random_number:
            guess_attempts -= 1
            print("Too high.\nGuess again.")
        elif user_guess < random_number:
            guess_attempts -= 1
            print("Too low.\nGuess again.")

        if guess_attempts == 0:
            should_continue_guessing = False
            print("You've run out of guesses, you lose")


elif user_choice == "hard":
    guess_attempts = 5
    should_continue_guessing = True

    while should_continue_guessing:
        print(f"You have {guess_attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        if user_guess == random_number:
            print(f"You got it! The answer was {user_guess}.")
            should_continue_guessing = False
        elif user_guess > random_number:
            guess_attempts -= 1
            print("Too high.\nGuess again.")
        elif user_guess < random_number:
            guess_attempts -= 1
            print("Too low.\nGuess again.")

        if guess_attempts == 0:
            should_continue_guessing = False
            print("You've run out of guesses, you lose")

else:
    print("You have entered invalid number. Please enter valid number.")
