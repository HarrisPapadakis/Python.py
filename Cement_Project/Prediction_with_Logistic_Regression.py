import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from datetime import datetime

# Read Database
df = pd.read_csv("cement_bags.csv")

# Transformation of Dependent Variable
# Create a new column 'Defective': 1 if there is an issue, 0 if empty
df["Defective"] = df["Issues"].apply(lambda x: 0 if x == "" else 1)

# Feature Engineering
# Days until expiration
df["DaysToExpire"] = df["Expiration"].apply(lambda d: (datetime.strptime(d, "%Y-%m-%d").date() - datetime.today().date()).days)

# Features (X) and Target (y)
X = df[["Weight", "IsWet", "DaysToExpire"]]
X["IsWet"] = X["IsWet"].astype(int)  # Convert boolean to int
y = df["Defective"]

# -Split Partition Train/Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print("\n📈 Model Evaluation:")
print(classification_report(y_test, y_pred))

# Prediction of new  cement bag
def predict_new_bag(weight, is_wet, expiration_date):
    days_to_expire = (datetime.strptime(expiration_date, "%Y-%m-%d").date() - datetime.today().date()).days
    input_data = [[weight, int(is_wet), days_to_expire]]
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]
    print(f"\n🧪 Prediction for new bag:")
    print(f"  Weight: {weight} kg, Wet: {is_wet}, Expiration in {days_to_expire} days")
    print(f"  ➤ Predicted as {'DEFECTIVE' if prediction == 1 else 'OK'} (Probability: {prob:.2f})")

# Prediction example
predict_new_bag(50.0, False, "2025-08-01")
predict_new_bag(46.5, True, "2024-03-01")

