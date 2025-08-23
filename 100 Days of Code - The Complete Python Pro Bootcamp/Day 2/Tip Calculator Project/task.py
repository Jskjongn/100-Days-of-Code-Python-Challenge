print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percent = 1 + (tip / 100)
bill_per_person = bill / people
bill_with_tip = bill_per_person * tip_percent
total_bill = round(bill_with_tip, 2)

print(f"Each person should pay: ${total_bill}")
