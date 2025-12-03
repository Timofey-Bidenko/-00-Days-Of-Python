# calc
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

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

def calculator():
    num1 = safe_to_float(input("First number: "))
    if not num1:
        print(f'Error: your input is not a number!')
        return

    while True:
        print("\nAvailable operators:")
        print(", ".join(operators))

        op = input("Pick an operator: ")
        calculation_function = operators.get(op)

        if not calculation_function:
            print(f'Operator "{op}" does not exist. (Or isnt inmplemented here)')
            break

        num2 = safe_to_float(input("Next number: "))
        if not num2:
            print(f'Error: your input is not a number!')
            return

        result = calculation_function(num1, num2)

        print(f"{num1} {op} {num2} = {result}")

        again = input("Continue with result? (y/n): ").lower()
        if again == "y":
            num1 = result
        else:
            break

while True:
    calculator()
    if input("\nStart calculator? (y/n): ").lower() == "n":
        break