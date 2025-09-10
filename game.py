import random

def hangman():
    # Predefined list of words
    words = ["apple", "banana", "grapes", "orange", "mango"]
    word = random.choice(words)  # Randomly select a word
    
    guessed = []  # List to keep track of guessed letters
    tries = 6     # Number of allowed wrong guesses
    
    print("Welcome to Hangman!")
    print("_ " * len(word))  # Display blanks for the word
    
    while tries > 0:
        guess = input("\nGuess a letter: ").lower()
        
        # Check for single alphabet input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed:
            print("You already guessed that letter.")
            continue
        else:
            guessed.append(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            tries -= 1
            print(f"Wrong guess! Tries left: {tries}")
        
        # Show current progress
        display_word = ""
        for letter in word:
            if letter in guessed:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word.strip())
        
        # Check if word is guessed
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("\n❌ You ran out of tries. The word was:", word)

# Run the game
hangman()