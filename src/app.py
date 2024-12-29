import pandas as pd

# Load the dataset
file_path = "../data/Bariatric_incidents_attended_by_LFB_from_Jan_2009.xlsx"
data = pd.read_excel(file_path)

# Handle missing values
columns_to_fill = ["SpecialServiceTypeCategory", "WardCode", "WardName", "BoroughCode", "BoroughName"]
data[columns_to_fill] = data[columns_to_fill].fillna("Unknown")

# Verify data consistency
# Ensure PumpCount and Notional Cost are non-negative
data = data[(data["PumpCount"] >= 0) & (data["Notional Cost (£)"] >= 0)]

# Drop duplicates if any
data = data.drop_duplicates()

# Save cleaned data as CSV
output_file = "../clean_data/cleaned_data.csv"
data.to_csv(output_file, index=False)
print(f"Cleaned data saved to {output_file}")
