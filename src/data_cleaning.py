# The main purpose of this script is to clean up provided data as pandas to an efficient and easily readable format

import pandas as pd 

# Load raw data

raw_path = "data/raw/sales_data_raw.csv"
df = pd.read_csv(raw_path)

# Column names are converted to both undercase and spaced with underscores for coding consistency

def clean_column_names(df):
    df.columns = (
        df.columns.str.strip()
                 .str.lower()
                 .str.replace(" ", "_")
    )
    return df

# Remove unecessary spaces from certain fields that may create errors, Rows with missing data to be dropped for consistency

def remove_invalid_rows(df):
    df = df.dropna(subset=["price", "qty"])
    df = df[(df["price"] >= 0) & (df["qty"] >= 0)]
    return df

# Utilize existing functions

df = clean_column_names(df)

df = remove_invalid_rows(df)

# Cleaned data is pushed to a csv file

output_path = "data/processed/sales_data_clean.csv"
df.to_csv(output_path, index=False)

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())
