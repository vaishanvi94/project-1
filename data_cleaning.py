import pandas as pd

# Load CSV file
df = pd.read_csv("traffic_stops.csv")

# Drop empty columns
df.dropna(axis=1, how='all', inplace=True)

# Fill missing values
df['driver_age'].fillna(df['driver_age'].mean(), inplace=True)
df['driver_race'].fillna("Unknown", inplace=True)
df['stop_duration'].fillna("Unknown", inplace=True)

# ✅ Updated age group logic
df['age_group'] = pd.cut(
    df['driver_age'],
    bins=[0, 18, 25, 40, 60, 100],
    labels=["0-18", "19-25", "26-40", "41-60", "61+"],
    include_lowest=True
)

# Save cleaned data
df.to_csv("cleaned_traffic_stops.csv", index=False)
print("✅ Cleaned data saved successfully!")
