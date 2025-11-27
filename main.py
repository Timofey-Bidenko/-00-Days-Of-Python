import random

random_number = random.random()
print(f"Random 0-1: {random_number:.3f}")
random_int = random.randint(1, 100)
print(f"Random 1-100 (custom range + integer): {random_int}")
range_random_number = random.random() * 100
print(f"Random 0-100 (custom range): {range_random_number:.1f}")
print(f"Random 0-100 (custom range + rounded): {int(range_random_number)}")

# lists
list = ["burgers", "hotdogs", "string"]
list.append("text")
print(list[0]) # list indexes start with 0, just like in most programming languages; Already used to this.
print(list[1])
print(list[2])
print(list[3])

random_list_entry = random.choice(list)
print("Random list entry: " + random_list_entry)

print(list[-1]) # negative indexes also work, just like with strings in day 2
print(list[1:len(list)-1]) # the middle of the list

# nested lists
field = [
    [True, True, False],
    [False, False,  True],
    [False, True, False],
]
print("Lets test your luck (there's only 4/9 win chance!):")
print("ofc you can memorize and look it up - but that wouldn't be fun!")
selection = int(input(f"Select a row 1-{len(field)} "))
if type(selection) == type(123) and selection >= 1 and selection <= len(field):
    selectedRow = field[selection-1]
    selection = int(input(f"Select a column 1-{len(selectedRow)} "))
    if type(selection) == type(123) and selection >= 1 and selection <= len(selectedRow):
        selectedEntry = field[selection-1]
        if selectedEntry == True:
            print("You won!")
        else:
            print("You lost!")
    else:
        print("Invalid selection")
else:
    print("Invalid selection")