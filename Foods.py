# Create a list of favorite foods and assign it to the variable `my_foods`
my_foods = ["pizza", "pasta", "pasta", "fruits"]

# Create a copy of `my_foods` and assign it to `friends_foods`
# Using slicing ([:]) ensures that `friends_foods` is a separate list, not just a reference to `my_foods`
friends_foods = my_foods[:]

# Print a message introducing your list of favorite foods
print("My favorite foods are:")
# Print the `my_foods` list to display its items
print(my_foods)

# Print a message introducing your friend's list of favorite foods
print("\nMy friend's favorite foods are:")
# Print the `friends_foods` list to display its items
print(friends_foods)
