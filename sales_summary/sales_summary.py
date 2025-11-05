import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load the dataset
data = pd.read_csv("sales_data1.csv")
# Check for missing data
print("Missing Data:\n", data.isna().sum())
# Convert Date column to datetime format
data["Date"] = pd.to_datetime(data["Date"], format='%d/%m/%Y')
# Add a day of the week column
data["Day_of_Week"] = data["Date"].dt.day_name()
# Check the summary statistics
print("\nSummary Statistics:\n", data.describe())
# Group by Product and calculate total revenue and quantity sold
product_summary = data.groupby("Product").agg({"Revenue": "sum", "Quantity": "sum"})
print("\nProduct Summary:\n", product_summary)
# Plot the total revenue per product
product_summary["Revenue"].plot(kind="bar")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.title("Total Revenue per Product")
plt.show()