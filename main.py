# ways of passing arguments to the function
def greet(name, age):
    print(f"Hello {name}, you are {age}.")

greet("Alice", 20)            # positional
greet(age=20, name="Alice")   # keyword

def print_add(a, b):
    print(a+b)
# same result, so keywording parameters is useless
print_add(3, 9) # good as is
print_add(b=9, a=3) # useless; same result






def safe_to_int(string : str):
    result = ""

    for symbol in string:
        utf_code = ord(symbol)
        if utf_code < 48 or utf_code > 57: # it's NOT a number 0 to 9
            break
        result += symbol # it's a number 0 to 9

    if len(result) == 0:
        return False
    return int(result)


def get_next_birthday(age : int, calculationCallback : function):
    print("Want to count day until your next birthday?")
    goal = input('\t"Y" -> yes\n\tLeave blank -> no\n\tNumber -> until birthday at Number years\n').strip().upper()
    goalNum = safe_to_int(goal)
    if goal == "Y":
        goalNum = age + 1
    
    if not goalNum:
        return
    
    d, w, m = calculationCallback(age, goalNum)
    print(f"There's {d} days between your {age} and {goalNum} birthdays!\nThat's approximately the same as {w} weeks or {m} months!")
    


# very inaccurate as some years have less days and in general 365 days is 52+1/7 weeks
def time_between_years(yearA : int, yearB : int):
    delta_years = abs(yearA - yearB)

    days = delta_years * 365
    weeks = delta_years * 52
    months = delta_years * 12

    return days, weeks, months

age = safe_to_int(input("How old are you? "))
if age:
    get_next_birthday(age, time_between_years)