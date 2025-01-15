def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""  # Describes the function's purpose to return a formatted full name.
    full_name = f"{first_name} {last_name}"  
    return full_name.title()  # Converts the full name to title case (e.g., "jimi hendrix" to "Jimi Hendrix").

musician = get_formatted_name("jimi", "hendrix")  # Calls the function with arguments "jimi" and "hendrix".
print(musician)  # Prints the formatted name (should output "Jimi Hendrix").
