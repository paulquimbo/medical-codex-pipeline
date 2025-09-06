import pandas as pd
from datetime import datetime

# Import shared utility for saving DataFrames to CSV
from utils.common_functions import save_to_csv

# Load RxNorm dataset (pipe-delimited, no headers in source file)
rxnorm = pd.read_csv(
    "input/rxnorm/RXNATOMARCHIVE.RRF",
    sep="|",
    header=None,
    dtype=str
)

# Display structure and column metadata
rxnorm.info()

# Preview first 5 rows
print(rxnorm.head())

# Explore key columns by index
rxnorm[1]
rxnorm[2]
rxnorm[3]

# Create a simplified DataFrame with selected columns
shortrxnorm = rxnorm[[1, 2]].copy()

# Add timestamp column for tracking updates
shortrxnorm['last_updated'] = datetime.today().strftime('%m-%d-%Y')

# Rename columns for clarity and consistency
shortrxnorm = shortrxnorm.rename(columns={
    1: 'Code',
    2: 'Description'
})

#removing empty descriptions or nulls or blanks 
shortrxnorm = shortrxnorm[
    shortrxnorm['Description'].notna() & 
    (shortrxnorm['Description'].str.strip() != "")]

# Save cleaned subset to CSV using shared utility
save_to_csv(shortrxnorm, 'rxnorm_short.csv')