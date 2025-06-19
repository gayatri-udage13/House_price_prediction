import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

df = pd.read_csv("BostonHousing(1).csv")

os.makedirs("static", exist_ok=True)

# Correlation heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("static/correlation_heatmap.png")
plt.close()

# Price distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['price'], bins=30, kde=True, color='skyblue')
plt.title("Price Distribution")
plt.xlabel("Price ($1000s)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("static/price_distribution.png")
plt.close()
