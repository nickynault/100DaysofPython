print("Welcome to the tip calculator.")
bill = input("What was the total bill? \n$")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15?\n")
people = input("How many people would split the bill?\n")

bill = float(bill)
tip_percentage = float(tip_percentage)
people = float(people)

tip_percentage *= .10
tip = bill * tip_percentage
split = round((tip / people), 2)
split = "{:.2f}".format(split)

print(f"Each person should pay: ${split}")
