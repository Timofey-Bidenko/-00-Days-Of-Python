print("Hey! Complete the smallest imaginary maze without dying!")

choice = input("Lets go ... forward / left / right ?").lower()
if choice == "left":
    print("You died, bad luck!")
elif choice == "forward":
    print("At least we're still alive")
    choice = input("Lets go ... forward / left / right ?").lower()
    if choice == "forward":
        print("Win achieved")
    elif choice == "left" or choice == "right":
        print(f"You did a 360 flip to the {choice} and moved forward")
    else:
        print("Death of inactivity")
elif choice == "right":
    print("Facing right; It's blocked. Restart.")
else:
    print("You did nothing and starved to death.")