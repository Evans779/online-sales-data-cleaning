# ============================================
# Online Sales Data Cleaning Script
# Author: Evans Zvavamhari
# ============================================

import pandas as pd
import numpy as np

# Load dataset
file_path = "Online Sales Data.csv"  
df = pd.read_csv(file_path)

print("Initial shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Standardize text columns
df['Payment Method'] = df['Payment Method'].str.title().str.strip()
df['Region'] = df['Region'].str.title().str.strip()
df['Product Category'] = df['Product Category'].str.title().str.strip()

# Feature engineering
df['Revenue per Unit'] = df['Total Revenue'] / df['Units Sold']

# Save cleaned dataset
df.to_csv("Cleaned_Online_Sales_Data.csv", index=False)

print("Cleaning completed! Cleaned dataset saved.")
