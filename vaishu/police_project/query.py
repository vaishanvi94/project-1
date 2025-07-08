import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("police_data.db")

# Example: Top 5 violations
query1 = """
SELECT violation, COUNT(*) as total
FROM traffic_stops
GROUP BY violation
ORDER BY total DESC
LIMIT 5;
"""
print("Top 5 Violations:")
print(pd.read_sql(query1, conn))

# Example: Arrest rate by country
query2 = """
SELECT country_name,
       ROUND(SUM(CASE WHEN is_arrested = 1 THEN 1 ELSE 0 END)*100.0/COUNT(*), 2) AS arrest_rate
FROM traffic_stops
GROUP BY country_name;
"""
print("\nArrest Rate by Country:")
print(pd.read_sql(query2, conn))

conn.close()

