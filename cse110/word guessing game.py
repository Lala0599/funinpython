#word guessing game
#added random list of words
#added limitations to number of guesses 
#track letters which have been tried
#checks if the guesses are only alphabets

import random

def word_guessing_game():
    
    word_list = ["mosiah", "alma", "lehi", "jacob", "helaman", "temple", "charity", "abinadai"]
    
    secret_word = random.choice(word_list).lower()
    guess_count = 0
    max_guesses = 10
    used_letters = set()
    
    print("Welcome to the word guessing game!\n")
    print(f"Guess the {len(secret_word)}-letter word. You have {max_guesses} attempts.\n")
    
    while guess_count < max_guesses:
        hint = ["_"] * len(secret_word)
        print(f"Your hint is: {' '.join(hint)}")
        print(f"Attempts left: {max_guesses - guess_count}")
        print(f"Letters tried: {' '.join(sorted(used_letters)) if used_letters else 'None'}\n")
        
        guess = input("What is your guess? ").lower()
        
        if not guess.isalpha():
            print("Please enter letters only.\n")
            continue
        
        guess_count += 1
        used_letters.update(set(guess))
        
        if guess == secret_word:
            print(f"\nCongratulations! You guessed '{secret_word}' in {guess_count} guesses!")
            if guess_count == 1:
                print("Wow! A perfect guess!")
            elif guess_count <= len(secret_word):
                print("Great job!")
            return
               
        if len(guess) != len(secret_word):
            print(f"Sorry, your guess must be {len(secret_word)} letters long.\n")
            continue
        
    hint = []
    secret_letters = list(secret_word)
        
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint.append(guess[i].upper())
            secret_letters[i] = None
        else:
            hint.append("_")
    
    for i in range(len(secret_word)):
        if hint[i] == "_" and guess [i] in secret_letters:
            hint[i] = guess[i].lower()
            secret_letters[secret_letters.index(guess[i])] = None        
    
    print(f"Your hint is: {' '.join(hint)}\n")
    
    correct = sum(1 for h in hint if h.isupper())
    if correct >= len(secret_word)/2:
        print("You're getting close! Many correct positions.")

    print(f"\nGame over! The secret word is '{secret_word.capitalize()}'")

        
word_guessing_game()