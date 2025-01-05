# Ask the user to input their height in centimeters and store it in the variable `heigh`
heigh = input("How tall are you, in centimeters?")

# Convert the input (which is a string) into an integer for comparison
heigh = int(heigh)  # Note: Fixed the typo from 'height' to 'heigh'

# Check if the height is greater than or equal to 140 cm
if heigh >= 140:
    # If the height is sufficient, print a message indicating they are tall enough
    print("\nYou are tall enough to ride!")
else:
    # If the height is insufficient, print a message encouraging them to try later
    print("\nYou will be able to ride when you are a little older.")
