import pandas as pd
from datetime import datetime

# Import shared utility for saving DataFrames to CSV
from utils.common_functions import save_to_csv

# Load SNOMED CT description file (tab-delimited, limited to 100,000 rows for testing)
snomed = pd.read_csv(
    'input/snomed/sct2_Description_Full-en_US1000124_20250301.txt',
    sep='\t',
    nrows=100000
)

# Display structure and column metadata
snomed.info()

# Preview first 5 rows
print(snomed.head())

# Explore key columns
snomed['id']
snomed['term']
snomed['caseSignificanceId']

# Create a simplified DataFrame with selected columns
shortsnomed = snomed[['id', 'term']].copy()

# Add timestamp column for tracking updates
shortsnomed['last_updated'] = datetime.today().strftime('%m-%d-%Y')

# Rename columns for clarity and consistency
shortsnomed = shortsnomed.rename(columns={
    'id': 'Code',
    'term': 'Description'
})

# Remove duplicate rows
shortsnomed = shortsnomed.drop_duplicates()

# Filter out empty or null descriptions
shortsnomed = shortsnomed[
    shortsnomed['Description'].notna() &
    (shortsnomed['Description'].str.strip() != "")
]

# Save cleaned subset to CSV using shared utility
save_to_csv(shortsnomed, 'snomed_short.csv')