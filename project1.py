# House Price Prediction using Linear Regression

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# -----------------------------
# Load Dataset
# -----------------------------
import os
print(os.getcwd())

df = pd.read_csv("Housing.csv")


print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# Data Preprocessing
# -----------------------------

# Convert categorical columns into numbers
df = pd.get_dummies(df, drop_first=True)

# -----------------------------
# Feature Selection
# -----------------------------
X = df.drop("price", axis=1)
y = df["price"]

# -----------------------------
# Train Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Model Training
# -----------------------------
model = LinearRegression()

model.fit(X_train, y_train)

# -----------------------------
# Prediction
# -----------------------------
y_pred = model.predict(X_test)

print("\nPredicted Prices:")
print(y_pred[:10])

# -----------------------------
# Model Evaluation
# -----------------------------
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance")
print("------------------")
print("MAE  :", mae)
print("MSE  :", mse)
print("RMSE :", rmse)
print("R2 Score :", r2)

# -----------------------------
# Visualization 1
# Actual vs Predicted
# -----------------------------
plt.figure(figsize=(8,6))

plt.scatter(y_test, y_pred)

plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")

plt.show()

# -----------------------------
# Visualization 2
# Correlation Heatmap
# -----------------------------
plt.figure(figsize=(10,8))

sns.heatmap(df.corr(),
            annot=True,
            cmap="coolwarm")

plt.title("Correlation Heatmap")

plt.show()
#----
# -----------------------------
# Visualization 3
# Feature Importance
# -----------------------------
coefficients = pd.DataFrame(
    model.coef_,
    X.columns,
    columns=["Coefficient"]
)

coefficients = coefficients.sort_values(
    by="Coefficient",
    ascending=False
)

plt.figure(figsize=(10,6))

plt.barh(
    coefficients.index[:10],
    coefficients["Coefficient"][:10]
)

plt.title("Top Features Affecting House Price")

plt.xlabel("Coefficient Value")

plt.show() 