# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Works until age 90

max_age = 90

max_days = max_age * 365
max_weeks = max_age * 52
max_months = max_age * 12

days = int(age) * 365
weeks = int(age) * 52
months = int(age) * 12



days_left = max_days - days
weeks_left = int(max_weeks - weeks)
months_left = int(max_months - months)

# without fstring
print("You have " + str(days_left) + " days, " + str(weeks_left) + " weeks, and " + str(months_left) + " months left.")

# fstring example 
print(f"You have  {days_left}  days, {weeks_left} weeks, and {months_left} months left.")