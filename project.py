# Caesar Cipher!

def caesar(text : str, shift : int):
    result = ""
    for symbol in text:
        if not symbol.isalpha():
            result += symbol
            continue
        
        utf_code = ord(symbol)
        utf_offset = ord("a")
        if utf_code >= 65 and utf_code <= 90: # it's an uppercase english letter
            utf_offset = ord("A")
        shifted = ord(symbol) - utf_offset  + shift
        shifted = shifted % 26
        result += chr(shifted + utf_offset)
    
    return result

text = input("Input message: ")
shift = int(input("Shift number: ")) % 26

print(f"Positive shift result (+{shift} usually encoded):\n{caesar(text, shift)}\n")
print(f"Negative shift result (-{shift} usually decoded):\n{caesar(text, -shift)}\n")