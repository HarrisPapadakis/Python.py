'''Import απαραίτητων βιβλιοθηκών 
Εισάγουμε τις βιβλιοθήκες Pandas, NumPy, και Matplotlib'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Διαβάζουμε το αρχείο CSV και το φορτώνουμε σε ένα DataFrame
data = pd.read_csv("sales_data1.csv")

# Ελέγχουμε αν υπάρχουν κενές τιμές στο dataset
print("Missing Data:\n", data.isna().sum())

# Μετατρέπουμε τη στήλη ημερομηνιών για να μπορούμε να κάνουμε χρονικές αναλύσεις
data["Date"] = pd.to_datetime(data["Date"], format='%d/%m/%Y')

# Δημιουργούμε μια νέα στήλη που περιέχει την ημέρα της εβδομάδας
data["Day_of_Week"] = data["Date"].dt.day_name()

# Εμφανίζουμε βασικά στατιστικά στοιχεία για τις αριθμητικές στήλες
print("\nSummary Statistics:\n", data.describe())

# Ομαδοποιούμε τα δεδομένα ανά προϊόν και υπολογίζουμε τα συνολικά έσοδα και την ποσότητα
product_summary = data.groupby("Product").agg({"Revenue": "sum", "Quantity": "sum"})
print("\nProduct Summary:\n", product_summary)

# Δημιουργούμε ένα ραβδόγραμμα για να δείξουμε τα συνολικά έσοδα ανά προϊόν
product_summary["Revenue"].plot(kind="bar")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.title("Total Revenue per Product")
plt.show()
