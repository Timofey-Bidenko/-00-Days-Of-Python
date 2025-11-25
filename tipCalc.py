# calc is short for calculator btw
print("Tip calc!")

bill = float(input("Total bill $?"))
tip_percent = float(input("How much % do you want to tip?"))
people = int(input("How many people split the bill?"))

tip = bill * tip_percent / 100
total = bill + tip # bill * (1 + tip_percent/100)
total_bill_per_person = total / people
# total_tip_per_person = (total - bill) / people # total - bill can be called Delta btw
total_tip_per_person = tip / people
print(f"Everyone shall pay {total_bill_per_person:.2f}$ or, if just the tip: {total_tip_per_person:.2f}$")