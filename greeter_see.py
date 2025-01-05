# Create a prompt message to explain to the user why their name is being requested
prompt = "If you tell us who you are, we can personalize the messages you"

# Add an additional line to the prompt to ask for the user's first name
prompt += "\nWhat is your first name? "

# Ask the user to enter their name using the custom prompt and store it in the variable `name`
name = input(prompt) 

# Use an f-string to display a personalized greeting message using the provided name
print(f"\nHello, {name}!") 
