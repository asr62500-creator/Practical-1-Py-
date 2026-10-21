
from datetime import datetime, date

# Display current date and time
now = datetime.now()

print("Current Date and Time:", now)
print("Current Date:", now.date())
print("Current Time:", now.strftime("%H:%M:%S"))

# Input date of birth
dob_input = input("Enter your date of birth (DD-MM-YYYY): ")
dob = datetime.strptime(dob_input, "%d-%m-%Y").date()

# Calculate age
today = date.today()

age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("Your Age is:", age, "years")
