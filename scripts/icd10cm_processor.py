import pandas as pd

# using common function to save to csv
from utils.common_functions import save_to_csv

# Loading Data Set and with no headers, will use fixed-with  format
## Assing column names to the dataframe
icd10us = pd.read_fwf('input/icd10US/icd10cm_order_2026_US.txt', 
                      header=None,
                      names=['Number', 'Code', 'Level', 'Description1', 'Description2'])


# Dispays rows and column information of the dataframe
icd10us.info()

# Displays the first 5 rows of the dataframe
print(icd10us.head())

# Column Exploration and checking potential columns to be used
## Displays the column information of the dataframe
icd10us.Number
icd10us.Code
icd10us.Level
icd10us.Description1


### Selecting columns of interest and adding to a new dataframe
shorticd10us = icd10us[['Code', 'Description1']]

# adding a new column to the new dataframe with a default value
shorticd10us ['last_updated'] = '09-05-2025'

# renaming column names from shortlist
shorticd10us = shorticd10us.rename(columns={
        'Description1': 'Description'
})

shorticd10us

save_to_csv(shorticd10us, 'icd10us_short.csv')