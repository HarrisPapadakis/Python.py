import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("cement_bags.csv")

# Histogram: Weight allocation
plt.figure(figsize=(8, 4))
plt.hist(df["Weight"], bins=10, color="skyblue", edgecolor="black")
plt.title("Distribution of Bag Weights")
plt.xlabel("Weight (kg)")
plt.ylabel("Number of Bags")
plt.grid(True)
plt.tight_layout()
plt.show()

# Pie Chart: Problem rates
# Create a metrics for each problem
problem_counts = {
    "Unacceptable weight": df["Issues"].str.contains("Unacceptable weight").sum(),
    "Wet bag": df["Issues"].str.contains("Wet bag").sum(),
    "Expired": df["Issues"].str.contains("Expired").sum(),
    "OK": (df["Issues"] == "").sum()
}

# Filter out zeros for a clean chart
problem_counts = {k: v for k, v in problem_counts.items() if v > 0}

# Graphic
plt.figure(figsize=(6, 6))
plt.pie(problem_counts.values(), labels=problem_counts.keys(), autopct='%1.1f%%', startangle=90, colors=plt.cm.Set3.colors)
plt.title("Bag Quality Issues")
plt.tight_layout()
plt.show()

# Bar char: Frequency of each problem
plt.figure(figsize=(7, 4))
plt.bar(problem_counts.keys(), problem_counts.values(), color='coral', edgecolor='black')
plt.title("Number of Bags per Issue Type")
plt.ylabel("Number of Bags")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()
