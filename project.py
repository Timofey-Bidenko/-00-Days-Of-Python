# number guessing
import random

RANDOM_START = 0
RANDOM_END = 100
MAX_ATTEMPTS = 6

def safe_to_float(string : str):
    result = ""

    for symbol in string:
        utf_code = ord(symbol)
        if utf_code == 44 or utf_code == 46:
            result += "." # it's . or ,
            continue
        if utf_code < 48 or utf_code > 57: # it's NOT a number 0 to 9
            break
        result += symbol # it's a number 0 to 9

    if len(result) == 0:
        return False
    return int(result)

def play():
    print(f"I chose a number {RANDOM_START}-{RANDOM_END}; You must guess it within just {MAX_ATTEMPTS} attempts")
    number = random.randint(RANDOM_START, RANDOM_END)
    best_guess_min, best_guess_max = RANDOM_START, RANDOM_END
    attempts = MAX_ATTEMPTS
    guessed = False

    while attempts > 0 and not guessed:
        print(f"You have {attempts} attempts!")
        print(f"Smart range: {best_guess_min}-{best_guess_max}")
        guess = int(safe_to_float(input("Guessing time! (Leave blank to end the game)\n")))
        if not guess:
            break
        if guess > best_guess_max or guess < best_guess_min:
            print(f"Guessing out of smart range ({best_guess_min}-{best_guess_max})!")
            continue

        if guess == number:
            guessed = True
            print("yay! You guessed it!")
            break
        
        attempts -= 1

        if guess > number:
            best_guess_max = guess

            if guess > number + 10:
                print("Your guess is bigger than my number")
                continue
            print("Your guess is slightly bigger than my number")
        elif guess < number:
            best_guess_min = guess

            if guess < number - 10:
                print("Your guess is smaller than my number")
                continue
            print("Your guess is slightly smaller than my number")
    
    if not guessed:
        print(f"You lose! The number was {number}.")
        

while True:
    if input('Guess a number? "y" for yes; skip to end\n').strip().lower() == "y":
        play()
    else:
        break