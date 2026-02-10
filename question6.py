import pandas as pd

# Load the crime dataset
df = pd.read_csv("crime.csv")

# Create the risk column based on violent crime levels
df["risk"] = df["ViolentCrimesPerPop"].apply(
    lambda x: "High-Crime" if x >= 0.50 else "LowCrime"
)

# Group by risk and calculate average unemployment rate
avg_unemployment = df.groupby("risk")["PctUnemployed"].mean()

# Print the results in a clear format
for risk_level, avg_value in avg_unemployment.items():
    print(risk_level + " average unemployment rate:", round(avg_value, 3))
