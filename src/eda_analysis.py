import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data from clean_data folder
data = pd.read_csv("../clean_data/cleaned_data.csv")

# View the first few rows
print(data.head())

print("*************************************************")

# Group by borough and count incidents
borough_counts = data.groupby('BoroughName')['CalYear'].count().sort_values(ascending=False)

# Top 5 boroughs
top_boroughs = borough_counts.head(5)

print("Top 5 Boroughs by Incident Count:")
print(top_boroughs)

top_boroughs.plot(kind='bar', title="Top 5 Boroughs by Incident Count")
plt.xlabel("Borough")
plt.ylabel("Number of Incidents")
plt.show()

# Analyze correlation between pump count and pump minutes
correlation = data[['PumpCount', 'PumpMinutesRounded']].corr()
print("Correlation Matrix:")
print(correlation)

# Scatter plot
data.plot.scatter(x='PumpCount', y='PumpMinutesRounded', title="Pump Count vs Pump Minutes")
plt.show()


# Group by year and count incidents
yearly_trends = data.groupby('CalYear')['CalYear'].count()

# Line plot for yearly trends
yearly_trends.plot(kind='line', marker='o', title="Yearly Trend of Incidents")
plt.xlabel("Year")
plt.ylabel("Number of Incidents")
plt.show()


# Aggregate pump minutes by borough
resource_usage = data.groupby('BoroughName')['PumpMinutesRounded'].sum().sort_values(ascending=False)

# Top 5 boroughs by resource usage
top_resource_usage = resource_usage.head(5)

print("Top 5 Boroughs by Resource Usage:")
print(top_resource_usage)

# Visualize
top_resource_usage.plot(kind='pie', autopct='%1.1f%%', title="Resource Usage by Borough")
plt.ylabel("")  # Hide y-label for a cleaner look
plt.show()
