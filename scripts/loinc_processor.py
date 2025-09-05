import pandas as pd

# Loading Data Set and have it as a variable
loinc = pd.read_csv('input/loinc/Loinc.csv')

# Dispays rows and column information of the dataframe
loinc.info()

# Displays the first 5 rows of the dataframe
print(loinc.head())

# Column Exploration and checking potential columns to be used
## Displays the column information of the dataframe
loinc.LOINC_NUM
loinc.LONG_COMMON_NAME
loinc.SHORTNAME
loinc.DisplayName
loinc.DefinitionDescription

### Selecting columns of interest and adding to a new dataframe
shortloinc = loinc[['LOINC_NUM', 'LONG_COMMON_NAME']]

# adding a new column to the new dataframe with a default value
shortloinc ['last_updated'] = '09-04-2025'

# renaming column names from shortlist
shortloinc = shortloinc.rename(columns={
    'LOINC_NUM': 'Code',
    'LONG_COMMON_NAME': 'Description'
})

shortloinc

shortloinc.to_csv('output/csv/loinc_short.csv', index=False)