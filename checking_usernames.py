# List of current usernames in the system
current_users = ["admin", "john", "jaden", "emily", "jiraya",
                 "mike shinoda", "chester", "naruto", "kakashi"]

# Converting current usernames to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

# List of new users attempting to register (this list was missing in the original code)
new_users = ["Admin", "Jiraya", "sakura", "kiba", "john"]  # Example new users for the loop

# Loop to check if each new username is already taken
for new_user in new_users:
    # Convert the new user's name to lowercase and check if it exists in the current users list
    if new_user.lower() in current_users_lower:
        # Print message if the username is already taken
        print(f"The username \"{new_user}\" is already taken. Please enter a new username.")
    else:
        # Print message if the username is available
        print(f"The username \"{new_user}\" is available.")

# Create a list of current usernames in uppercase to display them in uppercase form
current_users_uppercase = [user.upper() for user in current_users]

# Print the list of current users in uppercase
print(f"Current users in uppercase: {current_users_uppercase}")
