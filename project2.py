import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load CSV file
df = pd.read_csv('sales_data.csv')

# Display first few rows
print("Dataset:")
print(df.head())

# Basic statistics
print("\nSummary Statistics:")
print(df.describe())

# Calculate average sales
average_sales = df['Sales'].mean()
print(f"\nAverage Sales: {average_sales:.2f}")

# Calculate average profit
average_profit = df['Profit'].mean()
print(f"Average Profit: {average_profit:.2f}")

# ----------------------------
# Bar Chart
# ----------------------------
plt.figure(figsize=(8,5))
plt.bar(df['Product'], df['Sales'])
plt.title('Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.show()

# ----------------------------
# Scatter Plot
# ----------------------------
plt.figure(figsize=(8,5))
plt.scatter(df['Advertising'], df['Sales'])
plt.title('Advertising vs Sales')
plt.xlabel('Advertising Cost')
plt.ylabel('Sales')
plt.show()

# ----------------------------
# Heatmap (Correlation Matrix)
# ----------------------------
corr_matrix = df[['Sales', 'Profit', 'Advertising']].corr()

plt.figure(figsize=(6,5))
plt.imshow(corr_matrix, cmap='viridis', aspect='auto')
plt.colorbar()

plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)

for i in range(len(corr_matrix)):
    for j in range(len(corr_matrix)):
        plt.text(j, i,
                 f"{corr_matrix.iloc[i, j]:.2f}",
                 ha='center', va='center')

plt.title('Correlation Heatmap')
plt.show()