import polars as pl
from datetime import datetime

# Import shared utility for saving DataFrames to CSV
from utils.common_functions import save_to_csv

# Define path to NPI dataset
npicode_path = 'input/npi/npidata_pfile_20050523-20250810.csv'

# Load a sample of the dataset (first 1000 rows for testing)
npicode = pl.read_csv(npicode_path, n_rows=1000)

# Display basic dataset info
print(f"Loaded {len(npicode)} records")
print(f"Columns: {npicode.columns}")
print(f"Shape: {npicode.shape}")
print("\n Preview:")
print(npicode.head())

# Select relevant columns
shortnpicode = npicode.select([
    'NPI',
    'Provider Organization Name (Legal Business Name)',
    'Provider First Name',
    'Provider Last Name (Legal Name)'
]).clone()

# Add timestamp column
today = datetime.today().strftime('%m-%d-%Y')
shortnpicode = shortnpicode.with_columns([
    pl.lit(today).alias("last_updated")
])

# Add full name column
shortnpicode = shortnpicode.with_columns([
    (pl.col('Provider First Name') + ' ' + pl.col('Provider Last Name (Legal Name)')).alias('Full Name')
])

print(shortnpicode.head())

# Create organization-based subset
shortnpicode_org = shortnpicode.select([
    'NPI',
    'Provider Organization Name (Legal Business Name)',
    'last_updated'
]).rename({
    'NPI': 'Code',
    'Provider Organization Name (Legal Business Name)': 'Description'
}).filter(
    pl.col("Description").is_not_null() &
    (pl.col("Description").str.strip_chars() != "")
).clone()

print(shortnpicode_org.head())

# Create full-name-based subset
shortnpicode_full = shortnpicode.select([
    'NPI',
    'Full Name',
    'last_updated'
]).rename({
    'NPI': 'Code',
    'Full Name': 'Description'
}).filter(
    pl.col("Description").is_not_null() &
    (pl.col("Description").str.strip_chars() != "")
).clone()

print(shortnpicode_full.head())

# Save both subsets to CSV
save_to_csv(shortnpicode_org, "npicode_org_short.csv") 
save_to_csv(shortnpicode_full,"npicode_full_short.csv")
