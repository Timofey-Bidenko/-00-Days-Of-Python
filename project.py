#   Hangman!
"""
first of all we must describe our goal/task with all the challenging parts solved using just words and thinking ahead; Making this a multiline comment (unassigned literal string)

1. Pick a random word
2. Create blanks e.g.: _ _ _ _ _ _
3. while playing do input("Guess a letter") save a guessed letter and make sure it can't be used later on; playing = failed_guesses < 3 and blanks > 0
3_1.    If guess is correct -> yay
3_2.    Otherwise failed_guesses+=1
4. while has ended; if failed_guesses >= 3: "You lost!" else: "Winner"
"""

import random

stages = [
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n      |\n      |\n      |\n      |\n      |\n=========",
]


words = ["rock", "block", "hotdog", "burger", "pencil", "pen", "ruler", "book", "laptop", "water", "fire", "flame", "lava", "light", "ice", "smoke", "gas", "floor", "ceiling", "subject", "script", "line", "function", "word", "indentation", "sequence", "algorithm", "loop", "apple", "simple", "fast", "complicated", "slow", "big", "small", "cool", "lame", "lime", "lemon", "energy", "velocity", "turn", "text", "number", "true", "false", "raw", "cooked", "seasoned", "steak", "pepper", "lock", "work", "game", "life", "mine", "snake", "purple", "white", "yellow", "green", "blue", "pink", "black", "gray", "red", "orange", "cyan", "rainbow", "rain", "drop", "perfect", "long"]

word = random.choice(words)
print(word)
guessed = ["_"]*len(word) # must use array, because "_"*len(word) works, but we can't assing to strings (can't do string[index] = value)

used_letters = []
allowed_lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")
failed_guesses = 0
max_failed_guesses = len(stages) - 1
blanks = len(word)

print(f"The word is {len(word)} letters long!\n\n\n{"".join(guessed)}")

while failed_guesses < max_failed_guesses and blanks > 0:
    if len(used_letters) > 0:
        print(f"\n\nAlready used letters: {", ".join(used_letters)};")
    
    guess = input("Guess a letter! ").lower().strip()
    if guess == "":
        print("Your input was empty")
        continue
    guess = guess[0]

    guess_is_valid = False
    for allowed_lowercase_letter in allowed_lowercase_letters:
        if allowed_lowercase_letter == guess:
            guess_is_valid = True
            break
    if not guess_is_valid:
        print(f'Character "{guess}", is invalid; Your guess must be an english letter!')
        continue



    guess_already_used = False
    for used_letter in used_letters:
        if used_letter == guess:
            guess_already_used = True
            break
    if guess_already_used:
        print(f'Letter "{guess}", was already used')
        continue
    used_letters.append(guess)



    guess_failed = True
    for i in range(len(word)):
        if guess == word[i]:
            guess_failed = False
            guessed[i] = guess
            blanks -= 1

    if guess_failed:
        print("Guessed wrong!")
        failed_guesses += 1
    
    print("".join(guessed))
    print(stages[max_failed_guesses-failed_guesses])
        

if failed_guesses >= max_failed_guesses:
    print(f'You lost! The word was "{word}"')
else:
    print(f"Word guessed!")