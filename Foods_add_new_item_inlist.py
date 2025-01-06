# Create a list of favorite foods and assign it to the variable `my_foods`
my_foods = ["pizza", "pasta", "pasta", "fruits"]

# Create a copy of `my_foods` and assign it to `friends_foods`
# Using slicing ([:]) ensures that the two lists are independent
friends_foods = my_foods[:]

# Add a new food item to the `my_foods` list
my_foods.append("burgers")

# Add a different food item to the `friends_foods` list
friends_foods.append("fish")

# Print the header for the list of favorite foods for yourself
print("My favorite foods are:")
# Print the `my_foods` list to show all items, including the newly added one
print(my_foods)

# Print the header for the list of favorite foods for your friend
print("\nMy friend's favorite foods are:")
# Print the `friends_foods` list to show all items, including the newly added one
print(friends_foods)
