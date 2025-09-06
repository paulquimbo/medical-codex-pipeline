import pandas as pd

# using common function to save to csv
from utils.common_functions import save_to_csv

# Reading the SNOMED CT description file into a pandas dataframe and limiting to first 10,000 rows for testing
# add sep and encoding parameters when reading the csv file
snomed = pd.read_csv('input/snomed/sct2_Description_Full-en_US1000124_20250301.txt', sep='\t', nrows=5000)


# Dispays rows and column information of the dataframe
snomed.info()

# Displays the first 5 rows of the dataframe
print(snomed.head())


# Column Exploration and checking potential columns to be used
## Displays the column information of the dataframe
snomed.id
snomed.term
snomed.caseSignificanceId

### Selecting columns of interest and adding to a new dataframe
shortsnomed = snomed[['id', 'term']]

# adding a new column to the new dataframe with a default value
shortsnomed ['last_updated'] = '09-05-2025'

# renaming column names from shortlist
shortsnomed = shortsnomed.rename(columns={
        'id': 'Code',
        'term': 'Description'})

shortsnomed

save_to_csv(shortsnomed, 'snomed_short.csv')