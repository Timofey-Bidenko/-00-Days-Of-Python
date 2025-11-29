# function and recursion with parameters!
def countdown(number):
    if not number or number < 0:
        return
    print(number)
    countdown(number - 1)

countdown(12)

# woah typization specification is same as in Luau (using ":" after a parameter)!
def multiply_string(string : str, amount : int):
    result = ""
    for _ in range(amount):
        result += string
    return result

print(multiply_string("Hello World! ", 12))

# countdown without recursion; using a while loop
count = 12
while count > 0:
    print(count)
    count -= 1