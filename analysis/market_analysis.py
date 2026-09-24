import pandas as pd
import matplotlib.pyplot as plt

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
renewable_share = (
    df[["State", "Renewable_Share"]]
    .sort_values("Renewable_Share", ascending=False)
)

print("\nRenewable Energy Share:")
print(renewable_share)

# Display electricity prices
electricity_prices = (
    df[["State", "Average_Electricity_Price_Cents_kWh"]]
    .sort_values(
        "Average_Electricity_Price_Cents_kWh",
        ascending=False
    )
)

print("\nAverage Electricity Price:")
print(electricity_prices)

# Create renewable energy share chart
plt.figure(figsize=(8, 5))

plt.bar(
    renewable_share["State"],
    renewable_share["Renewable_Share"]
)

plt.title("Renewable Energy Share by State")
plt.xlabel("State")
plt.ylabel("Renewable Generation (%)")
plt.tight_layout()

plt.savefig("renewable_energy_share.png")
plt.show()
# Create electricity price chart
plt.figure(figsize=(8, 5))

plt.bar(
    electricity_prices["State"],
    electricity_prices["Average_Electricity_Price_Cents_kWh"]
)

plt.title("Average Electricity Price by State")
plt.xlabel("State")
plt.ylabel("Electricity Price (cents/kWh)")
plt.tight_layout()

plt.savefig("average_electricity_price.png")
plt.show()
# Generate key market insights
highest_renewable = renewable_share.iloc[0]
lowest_renewable = renewable_share.iloc[-1]

highest_price = electricity_prices.iloc[0]
lowest_price = electricity_prices.iloc[-1]

print("\nKey Market Insights:")

print(
    f"- {highest_renewable['State']} has the highest renewable "
    f"energy share at {highest_renewable['Renewable_Share']:.1f}%."
)

print(
    f"- {lowest_renewable['State']} has the lowest renewable "
    f"energy share at {lowest_renewable['Renewable_Share']:.1f}%."
)

print(
    f"- {highest_price['State']} has the highest average "
    f"electricity price at "
    f"{highest_price['Average_Electricity_Price_Cents_kWh']:.2f} cents/kWh."
)

print(
    f"- {lowest_price['State']} has the lowest average "
    f"electricity price at "
    f"{lowest_price['Average_Electricity_Price_Cents_kWh']:.2f} cents/kWh."
)