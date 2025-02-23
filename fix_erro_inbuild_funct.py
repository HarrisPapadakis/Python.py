def build_person(first_name, last_name, age=None):
    """Return a dictionary containing details about a person."""  
    
    # Create a dictionary with the first and last name
    person = {"first": first_name, "last": last_name}  
    
    # If age is provided, add it to the dictionary
    if age:
        person["age"] = age  
    
    return person  # Return the completed dictionary

# Create a dictionary for musician Jimi Hendrix, including age
musician = build_person("jimi", "hendrix", 27)  
print(musician)  # Output: {'first': 'jimi', 'last': 'hendrix', 'age': 27}
