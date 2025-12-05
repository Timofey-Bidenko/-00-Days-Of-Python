
import math
# py has no block scope; so this is a global variable
if True:
    burgers = 6
print(burgers) # 6

# https://www.houseofmath.com/uk/encyclopedia/chysla-ta-velychyny/chysla/prosti-chysla-y-rozkladannya-na-mnozhnyky/shcho-take-prosti-chysla >>> How to get rid of >75% existing numbers while searching primes.

def is_number_prime(number : int, outputHidden : bool):
    is_prime = True

    if number > 1 and number % 2 == 1:
        stringified_number = f"{number}"
        last_number_symbol = int(stringified_number[len(stringified_number)-1])

        if last_number_symbol == 5 and number != 5:
            is_prime = False
        else:
            sqrt = math.ceil(math.sqrt(number))
            if sqrt > 2:
                for i in range(2, sqrt+1, 1):
                    if number % i == 0:
                        is_prime = False
                        break
            else:
                is_prime = number % 2 != 0
    elif number != 2:
        is_prime = False
    
    if not outputHidden:
        print(f"Number {number} {is_prime and "is" or "isn't"} Prime")
    
    return is_prime

prime_numbers = []
last_number = 0
amount = 100
while len(prime_numbers) < amount:
    last_number += 1
    if is_number_prime(last_number, True):
        prime_numbers.append(last_number)

print(f"The first {amount} prime numbers:\n", prime_numbers)