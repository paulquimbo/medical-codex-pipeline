import pandas as pd
from datetime import datetime

# Import shared utility for saving DataFrames to CSV
from utils.common_functions import save_to_csv

# Load fixed-width ICD-10 dataset (no headers in source file) Fixed-width formatted file
# Assign column names manually
icd10us = pd.read_fwf(
    'input/icd10US/icd10cm_order_2026_US.txt',
    header=None,
    names=['Number', 'Code', 'Level', 'Description1', 'Description2']
)

# Display structure and column metadata
icd10us.info()

# Preview first 5 rows
print(icd10us.head())

# Explore key columns (accessed via dot or bracket notation)
icd10us['Number']
icd10us['Code']
icd10us['Level']
icd10us['Description1']

# Create a simplified DataFrame with selected columns
shorticd10us = icd10us[['Code', 'Description1']].copy()

# Add timestamp column for tracking updates
shorticd10us['last_updated'] = datetime.today().strftime('%m-%d-%Y')

# Rename columns for clarity and consistency
shorticd10us = shorticd10us.rename(columns={
    'Description1': 'Description'
})

#removing empty descriptions or nulls or blanks 
shorticd10us = shorticd10us[
    shorticd10us['Description'].notna() & 
    (shorticd10us['Description'].str.strip() != "")
]

# Save cleaned subset to CSV using shared utility
save_to_csv(shorticd10us, 'icd10us_short.csv')