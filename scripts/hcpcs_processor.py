import pandas as pd
from datetime import datetime

# Import shared utility function for saving DataFrames to CSV
from utils.common_functions import save_to_csv

# Load HCPC dataset from Excel file
hcpc_df = pd.read_excel('input/hcpc/HCPC2025_OCT_ANWEB.xlsx')

# Display basic structure and column info
hcpc_df.info()

# Preview the first 5 rows
print(hcpc_df.head())

# Explore key columns (use bracket notation for headers with spaces)
hcpc_df['HCPC']
hcpc_df['LONG DESCRIPTION']
hcpc_df['SHORT DESCRIPTION']

# Create a trimmed DataFrame with selected columns
shorthcpc = hcpc_df[['HCPC', 'LONG DESCRIPTION']].copy()

# Add a timestamp column for tracking updates
shorthcpc['last_updated'] = datetime.today().strftime('%m-%d-%Y')

# Rename columns for clarity and consistency
shorthcpc = shorthcpc.rename(columns={
    'HCPC': 'Code',
    'LONG DESCRIPTION': 'Description'
})

# Save the cleaned subset to CSV using shared utility
save_to_csv(shorthcpc, 'hcpc_short.csv')