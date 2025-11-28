list = ["burgers", "hotdogs", "string"]
for item in list:
    print(item)

for i in range(len(list)):
    print(i, list[i])

# at first I though range produces an array; Turns out it's a separate class!
print(type(range(2)), type([0, 1, 2]))

daily_earnings_last_week = [542, 619, 426, 508, 1482, 1397]

highest = 0
for daily_revenue in daily_earnings_last_week:
    if daily_revenue > highest:
        highest = daily_revenue

print("Highest daily revenue last week:", highest)

for i in range(0, 5, 1): # same as using range(5)
    print(i)
for i in range(0, 10, 2): # step of 2
    print(i)
for i in range(1, 6): # same as using range(5) and doing +1 to all entries
    print(i)


# I scripted the FizzBuzz sometime earlier
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)