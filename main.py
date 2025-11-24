# Printing to the console

print("Hello World")
print("Text (This) and Number ->", 123)
print(2^4)

print("\nMulti\nline\nprint\n") # \n in the start/end for padding among other prints


### String methods / operations
# concatenation
name = "World"
print("Hello " + name + "!")
# length
print("Name Length:", len(name))
# slicing
print("Name First Letter:", name[0])
print("Bizzare way to get Names First Letter:", name[-len(name)]) # |-index| and |index| can not be greater than len(name) = error
print("Name Last Letter:", name[-1])
print("Maybe this works as reverse?", name[-1: -len(name)]) # NOPE it doesnt
print("Piece of name:", name[1: 3]) # get characters 2 and 3
# so called "f-strings" (I'd call them template strings)
print(f'The name "{name}" consists of {len(name)} characters')

# user input (using console)
# input always returns string (text)
username = input("Username?")
actionId = int(input(f"{username}, what actionId shall run?"))
print(f"*The {actionId} was executed, actionId pow2 is {actionId*actionId}*")

### assign and reassign
# number/int
number = 300
number += actionId # essentially the same as:
# number = number + actionId
print(f"number + actionId sum: {number}")
# strings / booleans
color = "red"
is_cool = True # use snake_case in python, although I hate it