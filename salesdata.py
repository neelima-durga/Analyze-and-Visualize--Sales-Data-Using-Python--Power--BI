import pandas as pd

# Create sample sales data
data = {
    "OrderID": [1, 2, 3, 4, 5],
    "Date": pd.date_range(start="2024-01-01", periods=5, freq="D"),
    "Product": ["Laptop", "Shoes", "Phone", "Shirt", "Tablet"],
    "Quantity": [2, 5, 3, 4, 1],
    "UnitPrice": [55000, 2000, 25000, 1500, 30000],
    "Region": ["South", "North", "East", "West", "South"]
}

df = pd.DataFrame(data)
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# 🔽 Save to CSV
df.to_csv("sales_data.csv", index=False)

print("✅ File saved as sales_data.csv")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- Step 1: Load the CSV ----------------
# Make sure sales_data.csv exists in the same folder as your script
# If not, give full path like r"C:\Users\LENOVO\Documents\sales_data.csv"
df = pd.read_csv("sales_data.csv")

# If your dataset has a Date column, convert to datetime
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.month   # extract month

# ---------------- Step 2: Monthly Sales ----------------
monthly_sales = df.groupby("Month")["Revenue"].sum()

plt.figure(figsize=(10, 5))
sns.barplot(x=monthly_sales.index, y=monthly_sales.values)
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()

# ---------------- Step 3: Top Products ----------------
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()
plt.show()