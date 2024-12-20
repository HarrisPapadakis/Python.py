# List of toppings that are available in the store
available_toppings = ["mushrooms", "olives", "green pepers", 
                      "pepperoni", "pineapple", "extra cheese"]

# List of toppings the customer has requested
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

# Loop through each topping in the customer's requested toppings
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:# Check if the requested topping is available in the store
        print(f"Adding {requested_topping}.")        # If available, print a message indicating the topping is being added

    else:
        print(f"Sorry, we don't have {requested_topping}.") # If not available, print a message apologizing for its unavailability

print("\nFinished making your pizza!")