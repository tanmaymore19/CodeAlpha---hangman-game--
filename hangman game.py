import random


def get_random_word():
    words = ["python", "hangman", "laptop", "cricket", "jungle"]
    return random.choice(words)


def display_status(wrong_guesses, guessed_letters, word):
    print(f"\nWrong guesses left: {6 - wrong_guesses}")
    print(f"Letters guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

    # Show the word with blanks for unguessed letters
    display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print(f"Word: {display}\n")


def is_word_complete(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)


def play_hangman():
    print("=" * 40)
    print("       Welcome to Hangman!")
    print("=" * 40)
    print("Guess the word before you run out of tries.")
    print("You have 6 wrong guesses allowed.\n")

    word = get_random_word()
    guessed_letters = set()
    wrong_guesses = 0

    while wrong_guesses < 6:
        display_status(wrong_guesses, guessed_letters, word)

        # Get a valid single letter from the player
        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter only.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different one.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Nice! '{guess}' is in the word.")
            if is_word_complete(word, guessed_letters):
                display_status(wrong_guesses, guessed_letters, word)
                print("Congratulations! You guessed the word correctly!")
                break
        else:
            wrong_guesses += 1
            remaining = 6 - wrong_guesses
            print(f"Oops! '{guess}' is not in the word. {remaining} wrong guess(es) remaining.")
    else:
        # Loop ended because wrong_guesses hit 6
        print(f"\nGame Over! You've been hanged.")
        print(f"The word was: {word}")

    print("\nThanks for playing!\n")


def main():
    while True:
        play_hangman()
        again = input("Play again? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print("See you next time!")
            break


if __name__ == "__main__":
    main()