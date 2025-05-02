import random
from datetime import datetime, timedelta
import math

# SETTINGS 
TOTAL_BAGS = 10  # Ho many bags will be created 

# Funcion to create random bags 
def generate_random_bag():
    weight = round(random.uniform(45, 55), 2)            # Random weight between 45kg and 55kg
    is_wet = random.choice([True, False])                # Random wet/dry
    expiration = datetime.today() + timedelta(days=random.randint(-100, 300))  # Random expiration
    expiration_str = expiration.strftime("%Y-%m-%d")
    return {
        "weight": weight,
        "is_wet": is_wet,
        "expiration": expiration_str
    }

# Quality check function 
def check_bag(bag):
    problems = []

    # Weight check (acceptable 48-52 kg)
    if not (48 <= bag["weight"] <= 52):
        problems.append("Unacceptable weight")

    # Moisture check
    if bag["is_wet"]:
        problems.append("Wet bag")

    # Expiration check
    try:
        exp_date = datetime.strptime(bag["expiration"], "%Y-%m-%d").date()
        if exp_date < datetime.today().date():
            problems.append("Expired")
    except ValueError:
        problems.append("Invalid date format")

    return problems

#Main program
bags = []

for _ in range(TOTAL_BAGS):
    bag = generate_random_bag()
    issues = check_bag(bag)
    bag["issues"] = issues
    bags.append(bag)

# Display results 
for i, bag in enumerate(bags, 1):
    print(f"\nBag {i}:")
    print(f"  Weight     : {bag['weight']} kg")
    print(f"  Wet        : {'Yes' if bag['is_wet'] else 'No'}")
    print(f"  Expiration : {bag['expiration']}")
    print(f"  Issues     : {bag['issues'] if bag['issues'] else 'None'}")
