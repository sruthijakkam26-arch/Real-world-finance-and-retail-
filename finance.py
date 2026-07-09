import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("finance_retail.csv")

# Display first 5 rows
print(df.head())

# Dataset information
print(df.info())

# Check missing values
print(df.isnull().sum())

# Summary statistics
print(df.describe())

# Total Sales by Category
sales = df.groupby("Category")["Sales"].sum()
print(sales)

# Bar Chart
sales.plot(kind="bar", figsize=(8,5))
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# Monthly Sales Trend
df["Date"] = pd.to_datetime(df["Date"])
monthly_sales = df.groupby(df["Date"].dt.month)["Sales"].sum()

monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

print("Finance and Retail Analysis Completed Successfully!")