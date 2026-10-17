import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load Dataset
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")


print("Duplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

df["Order Date"] = pd.to_datetime(df["Order Date"])

# Features (Input)
X = df[["Quantity", "Discount", "Profit"]]

# Target (Output)
y = df["Sales"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and Train Model
model = LinearRegression()
model.fit(X_train, y_train)

print("Model trained successfully!")

# Display coefficients
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

# Predict Sales
y_pred = model.predict(X_test)

print("\nFirst 10 Predicted Sales:")
print(y_pred[:10])

# -----------------------------
# Model Evaluation
# -----------------------------
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("R2 Score:", r2)

# -----------------------------
# Visualization
# -----------------------------
plt.figure(figsize=(10,5))

plt.plot(y_test.values[:100], label="Actual Sales")
plt.plot(y_pred[:100], label="Predicted Sales")

plt.title("Actual vs Predicted Sales")
plt.xlabel("Records")
plt.ylabel("Sales")
plt.legend()

plt.savefig("Sales_Prediction_Graph.png")
plt.show()
comparison = pd.DataFrame({
    "Actual Sales": y_test.values,
    "Predicted Sales": y_pred
})

print("\nActual vs Predicted")
print(comparison.head(10))
# Save predictions to CSV
comparison.to_csv("Predicted_Sales.csv", index=False)

print("\nPrediction file saved successfully!")