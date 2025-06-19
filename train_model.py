import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Use a simplified file name
file_name = "BostonHousing(1).csv"

# Load the dataset
df = pd.read_csv(file_name)
X = df.drop(columns=["price"])
y = df["price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("house_price_prediction.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as 'house_price_prediction.pkl'")
