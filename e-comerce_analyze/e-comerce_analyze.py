import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Read the CSV file
sales_data = pd.read_csv("sales_data2.csv")
# Calculate total revenue
total_revenue = (sales_data["price"] * sales_data["quantity"]).sum()
print(f"Total Revenue: $ {total_revenue}")
# Calculate the average order value
avg_order_value = sales_data.groupby("order_id")["price"].sum().mean()
print(f"Average Order Value: $ {avg_order_value:.2f}")
# Identify the top-selling products
product_sales = sales_data.groupby("product_id").agg({"quantity": "sum"}).reset_index()
product_sales = product_sales.sort_values(by="quantity", ascending=False)
top_selling_products = product_sales.head(5)
print("Top 5 Selling Products:")
print(top_selling_products)
# Visualize the top-selling products using a bar chart
plt.bar(top_selling_products["product_id"].astype(str), top_selling_products["quantity"])
plt.xlabel("Product ID")
plt.ylabel("Quantity Sold")
plt.title("Top 5 Selling Products")
plt.show()