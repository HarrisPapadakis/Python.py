import pandas as pd

# Store cement bags in CSV form
def save_bags_to_csv(bags, filename="cement_bags.csv"):
    rows = []
    for bag in bags:
        rows.append({
            "Weight": bag["weight"],
            "IsWet": bag["is_wet"],
            "Expiration": bag["expiration"],
            "Issues": ", ".join(bag["issues"])
        })
    df = pd.DataFrame(rows)
    df.to_csv(filename, index=False)
    print(f"\n✅ Saved {len(bags)} bags to '{filename}'.")

# Read and analyze cement bags
def analyze_bags_from_csv(filename="cement_bags.csv"):
    df = pd.read_csv(filename)
    print("\n📊 BAG QUALITY STATS")
    print("---------------------")
    print(f"Total Bags        : {len(df)}")
    print(f"Average Weight    : {df['Weight'].mean():.2f} kg")
    print(f"Wet Bags          : {df['IsWet'].sum()} bags")
    print(f"Expired Bags      : {(df['Issues'].str.contains('Expired')).sum()}")
    print(f"Defective Bags    : {(df['Issues'] != '').sum()}")

# Calling functions
save_bags_to_csv(bags)
analyze_bags_from_csv()
