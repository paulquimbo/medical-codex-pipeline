import pandas as pd
from datetime import datetime

# Import shared utility for saving DataFrames to CSV
from utils.common_functions import save_to_csv

# Load LOINC dataset from CSV file
loinc = pd.read_csv('input/loinc/Loinc.csv')

# Display structure and column metadata
loinc.info()

# Preview first 5 rows
print(loinc.head())

# Explore key columns (use dot or bracket notation)
loinc['LOINC_NUM']
loinc['LONG_COMMON_NAME']
loinc['SHORTNAME']
loinc['DisplayName']
loinc['DefinitionDescription']

# Create a simplified DataFrame with selected columns
shortloinc = loinc[['LOINC_NUM', 'LONG_COMMON_NAME']].copy()

# Add timestamp column for tracking updates
shortloinc['last_updated'] = datetime.today().strftime('%m-%d-%Y')

# Rename columns for clarity and consistency
shortloinc = shortloinc.rename(columns={
    'LOINC_NUM': 'Code',
    'LONG_COMMON_NAME': 'Description'
})

#removing empty descriptions or nulls or blanks 
shortloinc = shortloinc[
    shortloinc['Description'].notna() & 
    (shortloinc['Description'].str.strip() != "")]

# Save cleaned subset to CSV using shared utility
save_to_csv(shortloinc, 'loinc_short.csv')