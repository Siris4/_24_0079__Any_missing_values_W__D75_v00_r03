import pandas as pd

# File paths
file_path_tesla = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0079__Day75_GoogleData_Resampling_and_Visualizing_Time_Series_240819\NewProject\r00-r09 START\r00_env_START\TESLA Search Trend vs Price.csv'
file_path_btc_search = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0079__Day75_GoogleData_Resampling_and_Visualizing_Time_Series_240819\NewProject\r00-r09 START\r00_env_START\Bitcoin Search Trend.csv'
file_path_btc_price = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0079__Day75_GoogleData_Resampling_and_Visualizing_Time_Series_240819\NewProject\r00-r09 START\r00_env_START\Daily Bitcoin Price.csv'
file_path_unemployment_2004_2020 = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0079__Day75_GoogleData_Resampling_and_Visualizing_Time_Series_240819\NewProject\r00-r09 START\r00_env_START\UE Benefits Search vs UE Rate 2004-20.csv'

# Load the data into DataFrames
df_tesla = pd.read_csv(file_path_tesla)
df_btc_search = pd.read_csv(file_path_btc_search)
df_btc_price = pd.read_csv(file_path_btc_price)
df_unemployment_2004_2020 = pd.read_csv(file_path_unemployment_2004_2020)

# Step 1: Find and display rows with missing values
def find_missing_values(df, file_name):
    missing_rows = df[df.isnull().any(axis=1)]
    if missing_rows.empty:
        print(f"No missing values found in {file_name}")
    else:
        print(f"Missing values in {file_name}:")
        print(missing_rows)
        print("\n")

# Step 2: Remove rows with missing values
def remove_missing_values(df):
    df_cleaned = df.dropna()
    return df_cleaned

# Step 3: Recheck to ensure no more missing values
def recheck_missing_values(df, file_name):
    missing_rows = df[df.isnull().any(axis=1)]
    if missing_rows.empty:
        print(f"Recheck: No missing values found in {file_name}\n")
    else:
        print(f"Recheck: Missing values still found in {file_name}:")
        print(missing_rows)
        print("\n")

# Perform all steps on each DataFrame
def process_file(df, file_name):
    find_missing_values(df, file_name)
    df_cleaned = remove_missing_values(df)
    recheck_missing_values(df_cleaned, file_name)
    return df_cleaned

# Apply the process to each file
df_tesla_cleaned = process_file(df_tesla, 'TESLA Search Trend vs Price.csv')
df_btc_search_cleaned = process_file(df_btc_search, 'Bitcoin Search Trend.csv')
df_btc_price_cleaned = process_file(df_btc_price, 'Daily Bitcoin Price.csv')
df_unemployment_2004_2020_cleaned = process_file(df_unemployment_2004_2020, 'UE Benefits Search vs UE Rate 2004-20.csv')
