def build_person(first_name, last_name):
    """Return a dictionary with information about a person."""  # Describes the function's purpose to return a dictionary.
    person = {"first": first_name, "last": last_name}  # Creates a dictionary with keys "first" and "last".
    return person  # Returns the dictionary.

musician = build_person("jimi", "hendrix")  # Calls the function with arguments "jimi" and "hendrix".
print(musician)  # Prints the dictionary (should output {'first': 'jimi', 'last': 'hendrix'}).
