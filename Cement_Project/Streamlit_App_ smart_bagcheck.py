import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from datetime import datetime

# Load & Prepare Data 
@st.cache_data
def load_data():
    df = pd.read_csv("cement_bags.csv")
    df["Defective"] = df["Issues"].apply(lambda x: 0 if x == "" else 1)
    df["DaysToExpire"] = df["Expiration"].apply(lambda d: (datetime.strptime(d, "%Y-%m-%d").date() - datetime.today().date()).days)
    return df

df = load_data()

# Train model 
X = df[["Weight", "IsWet", "DaysToExpire"]]
X["IsWet"] = X["IsWet"].astype(int)
y = df["Defective"]
model = LogisticRegression()
model.fit(X, y)

# Web UI 
st.title("🧱 Smart Cement Bag Checker")

st.sidebar.header("🔍 Check a New Bag")
weight = st.sidebar.slider("Weight (kg)", 45.0, 55.0, 50.0)
is_wet = st.sidebar.selectbox("Is the bag wet?", [False, True])
expiration = st.sidebar.date_input("Expiration date", datetime.today())
days_to_expire = (expiration - datetime.today().date()).days

# Prediction 
if st.sidebar.button("Predict Quality"):
    input_data = [[weight, int(is_wet), days_to_expire]]
    pred = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]
    st.subheader("Prediction Result:")
    if pred == 1:
        st.error(f"❌ The bag is predicted to be DEFECTIVE ({prob:.2%} probability)")
    else:
        st.success(f"✅ The bag is predicted to be OK ({1 - prob:.2%} probability)")

#  Stats and Visualization 
st.markdown("## 📊 Dataset Overview")
st.dataframe(df.head())

st.markdown("## 📈 Bag Weight Distribution")
fig, ax = plt.subplots()
ax.hist(df["Weight"], bins=10, color="skyblue", edgecolor="black")
ax.set_xlabel("Weight (kg)")
ax.set_ylabel("Number of Bags")
st.pyplot(fig)

st.markdown("## 🧪 Defective Bag Breakdown")
issue_counts = {
    "Weight": df["Issues"].str.contains("Unacceptable weight").sum(),
    "Wet": df["Issues"].str.contains("Wet bag").sum(),
    "Expired": df["Issues"].str.contains("Expired").sum(),
    "OK": (df["Issues"] == "").sum()
}
labels = list(issue_counts.keys())
values = list(issue_counts.values())
fig2, ax2 = plt.subplots()
ax2.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
st.pyplot(fig2)
