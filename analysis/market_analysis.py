import pandas as pd

# Load the energy market data
df = pd.read_csv("data/energy_market_data.csv")

# Calculate renewable energy share
df["Renewable_Share"] = (
    df["Renewable_Generation_MWh"] / df["Net_Generation_MWh"] * 100
)

# Display the dataset
print("Energy Market Data:")
print(df)

# Display renewable share by state
print("\nRenewable Energy Share:")
print(
    df[["State", "Renewable_Share"]]
    .sort_values("Renewable_Share", ascending=False)
)

# Display electricity prices
print("\nAverage Electricity Price:")
print(
    df[["State", "Average_Electricity_Price_Cents_kWh"]]
    .sort_values(
        "Average_Electricity_Price_Cents_kWh",
        ascending=False
    )
)
