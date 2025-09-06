import pandas as pd

# using common function to save to csv
from utils.common_functions import save_to_csv

# Loading Data Set and have it as a variable
rxnorm = pd.read_csv("input/rxnorm/RXNATOMARCHIVE.RRF", sep="|", header=None, dtype=str)

# Dispays rows and column information of the dataframe
rxnorm.info()

# Displays the first 5 rows of the dataframe
print(rxnorm.head())

# Column Exploration and checking potential columns to be used
## Displays the column information of the dataframe
rxnorm[[1]]
rxnorm[[2]]
rxnorm[[3]]

### Selecting columns of interest and adding to a new dataframe
shortrxnorm = rxnorm[[1, 2]]

# adding a new column to the new dataframe with a default value
shortrxnorm ['last_updated'] = '09-05-2025'

# renaming column names from shortlist
shortrxnorm = shortrxnorm.rename(columns={
    1: 'Code',
    2: 'Description'
})


shortrxnorm

save_to_csv(shortrxnorm, 'rxnorm_short.csv')