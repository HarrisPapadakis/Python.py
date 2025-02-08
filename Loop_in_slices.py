# Define a list of players on the team
players = ['ronaldinho', 'messi', 'cristiano ronaldo', 'kross', 'sergio ramos', 'pineda']

# Display a message indicating the first three players will be shown
print("Here are the first three players on my team:")

# Loop through the first three players in the list
for player in players[0:3]:
    # Print each player's name with the first letter of each word capitalized
    print(player.title())
