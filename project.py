# PASSWORD GENERATOR
import random

print("Welcome to the password generator!")
print("Tip: Special characters are considered anything that isn't an english letter or a number 0 to 9")



total_password_length = input("\n\n(Leave this blank for advanced setup)\nHow long do you want your password to be?\n").strip()
use_advanced_setup = total_password_length == ""

amount_letters = 0
amount_numbers = 0
amount_symbols = 0

if use_advanced_setup:
    amount_letters = int(input("How many letters? "))
    amount_numbers = int(input("How many numbers? "))
    amount_symbols = int(input("How many special characters? "))
    total_password_length = amount_letters + amount_numbers + amount_symbols
else:
    total_password_length = int(total_password_length)
    total_available_characters = total_password_length

    if total_available_characters > 1:
        amount_letters = random.randint(1, total_available_characters)
        total_available_characters -= amount_letters

        if total_available_characters > 1:
            amount_numbers = random.randint(1, total_available_characters)
            total_available_characters -= amount_numbers

            amount_symbols = total_available_characters
        elif total_available_characters > 0:
            random_character_type = random.choice(["n", "s"])
            if random_character_type == "n":
                amount_numbers = 1
            elif random_character_type == "s":
                amount_symbols = 1
    else:
        random_character_type = random.choice(["l", "n", "s"])
        if random_character_type == "l":
            amount_letters = 1
        elif random_character_type == "n":
            amount_numbers = 1
        elif random_character_type == "s":
            amount_symbols = 1

print(f"Final password will consist of:\n\t- {amount_letters} english letter(s) (uppercase/lowercase)\n\t- {amount_numbers} number(s) (0-9)\n\t- {amount_symbols} special character(s) (your input)")
if not use_advanced_setup:
    print("Tip: You can restart and use advanced setup to set these amounts manually\n")



letters = list("abcdefghigklmnopqrstuvwxyz" + "abcdefghigklmnopqrstuvwxyz".upper())
numbers = list("0123456789")
# this is how I got the utf codes
#for l in letters:
#    print(l, ord(l))
#for n in numbers:
#    print(n, ord(n))

symbols = []
if amount_symbols > 0:
    symbols_input = list(input("Want to use any special characters? Maybe a different language, spaces, brackets, underscores, hashtags, etc? Write all special characters you would like to use here: "))
    print(len(symbols_input))
    
    for symbol in symbols_input:
        utf_code = ord(symbol)

        # prevent counting default characters as special; skip them
        if utf_code >= 65 and utf_code <= 90: # it's an uppercase english letter
            continue
        if utf_code >= 97 and utf_code <= 122: # it's a lowercase english letter
            continue
        if utf_code >= 48 and utf_code <= 57: # it's a number 0 to 9
            continue
        
        # I don't know how to do table.find, so here's my own O(n) implementation
        # so if a special character is already in use, we'll skip it as well
        symbol_already_in_use = False
        for used_symbol in symbols:
            if used_symbol == symbol:
                symbol_already_in_use = True
                break
        if symbol_already_in_use:
            continue

        symbols.append(symbol)
        

result = ""

for i in range(total_password_length):
    choices = []
    if amount_letters > 0:
        choices.append("l") # l = letters
    if amount_numbers > 0:
        choices.append("n") # n = number
    if amount_symbols > 0 and len(symbols) > 0:
        choices.append("s") # s = symbol
    
    chosen_type = random.choice(choices)
    if chosen_type == "l":
        amount_letters -= 1
        result += random.choice(letters)
    elif chosen_type == "n":
        amount_numbers -= 1
        result += random.choice(numbers)
    elif chosen_type == "s":
        amount_symbols -= 1
        result += random.choice(symbols)

print(f"Here's a password for you! {total_password_length} characters long.\n\n{result}\n\nHave a nice day!")