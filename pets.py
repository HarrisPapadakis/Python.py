def desrcibe_pet(animal_type, pet_name):
    """Display information about a pet."""  # This is a docstring explaining the function's purpose
    # Print the type of animal owned
    print(f"\nI have a {animal_type.title()}.")
    # Print the pet's name
    print(f"My {animal_type}'s name is {pet_name}. ")

# Call the function with the animal type as "lizard" and the pet name as "mitsos"
desrcibe_pet("lizard", "mitsos")
