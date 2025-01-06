# Define the variable `age` and assign it the value 12
age = 12

# Check if the age is less than 4
if age < 4:
    # If the condition is true, print that the admission cost is $0
    print("Your admission cost is $0.")
# Check if the age is less than 18 (and greater than or equal to 4 due to previous condition)
elif age < 18:
    # If the condition is true, print that the admission cost is $25
    print("Your admission cost is $25.")
# If none of the above conditions are true, execute the following
else:
    # Print that the admission cost is $40 for ages 18 or older
    print("Your admission cost is $40.")
