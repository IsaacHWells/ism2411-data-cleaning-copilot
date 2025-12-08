# The main purpose of this script is to clean up provided data as pandas to an efficient and easily readable format

import pandas as pd 

# Load raw data

raw_path = "data/raw/sales_data_raw.csv"
df = pd.read_csv(raw_path)

# Column names are converted to both undercase and spaced with underscores for coding consistency

df.columns = (
    df.columns.str.strip()        
             .str.lower()
             .str.replace(" ", "_")
)

# Remove unecessary spaces from certain fields that may create erros

field_check = ["prodname", "category"]
for cols in field_check:
    if cols in df.columns:
        df[cols] = df[cols].astype(str).str.strip()

# Rows with missing data to be dropped for consistency

df = df.dropna(subset=["price", "qty"])

# Rows with impossible data pulled, in order to avoid nonsencical negative values

df = df[(df["price"] >= 0) & (df["qty"] >= 0)]

# Cleaned data is pushed to a csv file

output_path = "data/processed/sales_data_clean.csv"
df.to_csv(output_path, index=False)
