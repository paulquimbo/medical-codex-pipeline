import polars as pl

# using common function to save to csv
from utils.common_functions import save_to_csv

#adding path to a data set
npicode_path = 'input/npi/npidata_pfile_20050523-20250810.csv'

#Loading Data Set with specified number of rows for testing
npicode = pl.read_csv(npicode_path, n_rows=1000)

print(f"Successfully loaded {len(npicode)} records from NPI data")
print(f"Columns: {npicode.columns}")
print(f"\nDataset shape: {npicode.shape}")
print(f"\nFirst 5 rows:")
print(npicode.head())

# Column Exploration and checking potential columns to be used
npicode.columns
## Displays the column information of the dataframe 
npicode['NPI']
npicode['Provider Organization Name (Legal Business Name)']
npicode['Provider Credential Text']
npicode['Provider First Name']
npicode['Provider Last Name (Legal Name)']

### Selecting columns of interest and adding to a new dataframe
shortnpicode = npicode[[
    'NPI', 
    'Provider Organization Name (Legal Business Name)', 
    'Provider First Name', 
    'Provider Last Name (Legal Name)'
    ]]

print(shortnpicode.head())

# adding a new column to the new dataframe with a default value using polars syntax
shortnpicode = shortnpicode.with_columns([
    pl.lit("09-05-2025").alias("last_updated")])

# Displays the first 5 rows of the dataframe
print(shortnpicode.head())

# adding a new column to the new dataframe with a full name
shortnpicode = shortnpicode.with_columns([
    (pl.col('Provider First Name') + ' ' + pl.col('Provider Last Name (Legal Name)')).alias('Full Name')
])

print(shortnpicode.head())



# Will create 2 types of dataframes, one with organization name and one with full name
    # NPI's for organization name
shortnpicode_org = shortnpicode[[
    'NPI', 
    'Provider Organization Name (Legal Business Name)', 
    'last_updated', 
    ]]

# renaming column names from shortlist
shortnpicode_org = shortnpicode_org.rename({
        'NPI': 'Code',
        'Provider Organization Name (Legal Business Name)': 'Description',
})

#removing empty descriptions or nulls or blanks 
shortnpicode_org = shortnpicode_org.filter(
    pl.col("Description").is_not_null() &
    (pl.col("Description").str.strip_chars()!=("")))


print(shortnpicode_org.head)




    # NPI's for full name
shortnpicode_full = shortnpicode[[
    'NPI', 
    'Full Name', 
    'last_updated', 
    ]]

# renaming column names from shortlist
shortnpicode_full = shortnpicode_full.rename({
        'NPI': 'Code',
        'Full Name': 'Description',
})

#removing empty descriptions or nulls or blanks 
shortnpicode_full = shortnpicode_full.filter(
    pl.col("Description").is_not_null() &
    (pl.col("Description").str.strip_chars()!=("")))

print(shortnpicode_full.head)





save_to_csv(shortnpicode_org, "npicode_org_short.csv")
save_to_csv(shortnpicode_full,"npicode_full_short.csv")