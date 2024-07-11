import random

def choose_difficulty():
    """
        Prompts the user to choose
        a difficulty level and returns
        the corresponding range and
        number of guesses.
    """
    print("Choose a difficulty level: ")
    print("1. Easy (1-10, 5 guesses)")
    print("2. Medium (1-50, 7 guesses)")
    print("3. Hard (1-100, 10 guesses)")

    while True:
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            return 1, 10, 5
        elif choice == '2':
            return 1, 50, 7
        elif choice == '3':
            return 1, 100, 10
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

def get_random_number(lower, upper):
    """
        Generates a random number
        within the specified range.
    """
    return random.randint(lower, upper)

def get_user_guess():
    """
        Prompts the user for a
        guess and returns it.
    """
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")

def provide_feedback(guess, target):
    """
        Provides feedback on
        whether the guess was too high,
        too low, or correct.
    """
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print("Correct!")

def play_game():
    """
        Main game loop: handles the
        gameplay, feedback, and win/
        loss scenarios.
    """
    lower, upper, max_attempts = choose_difficulty()
    target_number = get_random_number(lower, upper)
    attempts = 0

    print(f"\nI have selected a number between {lower} and {upper}. Can you guess it?")

    while attempts < max_attempts:
        guess = get_user_guess()
        attempts += 1
        provide_feedback(guess, target_number)

        if guess == target_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        else:
            remaining_attempts = max_attempts - attempts
            print(f"You have {remaining_attempts} attempts remaining.")
        
    if guess != target_number:
        print(f"Sorry, you've used all your attempts. The number was {target_number}.")
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again == 'yes':
            play_game()
        else:
            print("Thank you for playing! Goodbye!")

play_game()