#bill split calculator including tip

print("Welcome to the tip Calculator")

total_bill = input("What was the total bill? ")
total_bill_as_float = float(total_bill)

tip_percentage = input("What percentage would you like to give? 10,12 or 15?")
tip_percentage = f" 1.{tip_percentage}"
tip_percentage_as_float = float(tip_percentage)


people_split = input("How many to split the bill?")
people_split_as_int = int(people_split)

total_bill = total_bill_as_float * tip_percentage_as_float // people_split_as_int

total_bill_output = print(f"Each person should pay: ${total_bill}")