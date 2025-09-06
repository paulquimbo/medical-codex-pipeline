import pandas as pd
from datetime import datetime

# Import shared utility for saving DataFrames to CSV
from utils.common_functions import save_to_csv

# Load ICD-10 WHO dataset (semicolon-delimited, no headers in source file)
icd10who = pd.read_csv(
    'input/icd10WHO/icd102019syst_codes_WHO.txt',
    header=None,
    sep=';',         # Semicolon delimiter
    encoding='utf-8' # Adjust if encoding issues arise
)

# Display structure and column metadata
icd10who.info()

# Preview first 5 rows
print(icd10who.head())

# Rename default column indices to meaningful names
icd10who = icd10who.rename(columns={
    0: 'Num1',
    1: 'Let1',
    2: 'Let2',
    3: 'Num2',
    4: 'Code1',
    5: 'Code2',
    6: 'Code3',
    7: 'Code4',
    8: 'Code5',
    9: 'Code6',
    10: 'Description',
    11: 'Code7',
    12: 'Code8',
    13: 'Code9',
    14: 'Code10',
    15: 'Code12',
    16: 'Code13',
    17: 'Code14'
})

# Recheck structure after renaming
print(icd10who.head())
icd10who.info()

# Create a simplified DataFrame with selected columns
shorticd10who = icd10who[['Code3', 'Description']].copy()

# Add timestamp column for tracking updates
shorticd10who['last_updated'] = datetime.today().strftime('%m-%d-%Y')

# Rename columns for clarity and consistency
shorticd10who = shorticd10who.rename(columns={
    'Code3': 'Code'
})

#removing empty descriptions or nulls or blanks 
shorticd10us = shorticd10who[
    shorticd10who['Description'].notna() & 
    (shorticd10who['Description'].str.strip() != "")
]

# Save cleaned subset to CSV using shared utility
save_to_csv(shorticd10who, 'icd10who_short.csv')