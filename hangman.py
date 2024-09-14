import random


word_categories = {
    "Animals": ["elephant", "tiger", "giraffe", "kangaroo", "dolphin"],
    "Countries": ["canada", "brazil", "france", "germany", "india"],
    "Movies": ["inception", "titanic", "gladiator", "avatar", "matrix"]
}


hangman_graphics = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

def choose_word(category):
    """Select a random word from the chosen category."""
    return random.choice(word_categories[category])

def display_current_state(word, guessed_letters):
    """Display the current guessed state of the word."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def get_hint(word):
    """Provide a hint for the player."""
    hints = {
        "elephant": "It's a large mammal with a trunk.",
        "tiger": "A big cat with orange fur and black stripes.",
        "giraffe": "Tallest land animal with a long neck.",
        "kangaroo": "Marsupial known for hopping.",
        "dolphin": "Intelligent marine mammal.",
        "canada": "Country known for maple syrup.",
        "brazil": "Famous for the Amazon rainforest.",
        "france": "Eiffel Tower is located here.",
        "germany": "Famous for its beer and sausages.",
        "india": "Known for the Taj Mahal.",
        "inception": "A movie about dreams within dreams.",
        "titanic": "A ship that famously sank.",
        "gladiator": "Movie about a Roman general turned gladiator.",
        "avatar": "Movie set on the planet Pandora.",
        "matrix": "A hacker discovers the truth about reality."
    }
    return hints.get(word, "No hint available.")

def play_hangman():
    print("Welcome to Hangman!")
    print("Choose a category:")
    for idx, category in enumerate(word_categories.keys(), 1):
        print(f"{idx}. {category}")
    
    choice = int(input("Enter your choice: ")) - 1
    category = list(word_categories.keys())[choice]
    word = choose_word(category)

    print(f"You have chosen the category: {category}")
    print("Select difficulty level: ")
    print("1. Easy (10 guesses)")
    print("2. Medium (7 guesses)")
    print("3. Hard (5 guesses)")
    
    difficulty = int(input("Enter your choice: "))
    allowed_guesses = 10 if difficulty == 1 else 7 if difficulty == 2 else 5

    guessed_letters = set()
    incorrect_guesses = 0

    while incorrect_guesses < allowed_guesses:
        print(hangman_graphics[incorrect_guesses])
        print(f"Word: {display_current_state(word, guessed_letters)}")
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")
        print(f"Remaining guesses: {allowed_guesses - incorrect_guesses}")

        guess = input("Enter a letter (or type 'hint' for a hint): ").lower()

        if guess == "hint":
            print(f"Hint: {get_hint(word)}")
            incorrect_guesses += 1  
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1

    if incorrect_guesses == allowed_guesses:
        print(hangman_graphics[-1])
        print(f"Sorry, you lost! The word was: {word}")

if __name__ == "__main__":
    play_hangman()
