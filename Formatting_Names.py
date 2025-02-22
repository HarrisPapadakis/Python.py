def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted."""
    
    # Check if a middle name is provided
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    
    # Return the formatted name with title case
    return full_name.title()  # Moved outside of the if-else block for consistency

# Calling the function without a middle name
musician = get_formatted_name("jimi", "hendrix")
print(musician)  # Output: Jimi Hendrix

# Calling the function with a middle name
musician = get_formatted_name("john", "hooker", "lee")
print(musician)  # Output: John Lee Hooker
