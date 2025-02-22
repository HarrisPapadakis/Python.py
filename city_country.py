def city_country(city, country):   
    """Return a single string with the city and the country."""  
    
    # Fixed syntax error: Changed f{} to f"{}"
    return f"{city}, {country}"  

# Print city-country pairs
print(city_country("Athens", "Greece"))  
print(city_country("Paris", "France"))  
print(city_country("Tokyo", "Japan"))  
