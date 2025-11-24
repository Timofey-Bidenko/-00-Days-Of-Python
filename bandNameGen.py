print("Welcome to Generic Name Generator (GNG)")
# .strip to clear unnecessary spaces on the start/end of input
first_ever_username = input("What was your first ever username in games? Maybe the first one you can recall?").strip()
latest_username = input("What is your current username?").strip()
user_random = int(input("Pick any number!"))
# I figured out int() can be used to eventually round numbers
generic_name = first_ever_username[0 : int(len(first_ever_username) / 2)] + latest_username[int(len(latest_username) / 2) : len(latest_username)] + f"{int( (user_random + 3) *1212 / 93 )}"
print(f'Your Generic Name is "{generic_name}"')