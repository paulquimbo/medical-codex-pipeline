import pandas as pd

# using common function to save to csv
from utils.common_functions import save_to_csv

# Loading Data Set and with no headers, base on the raw data we see they are using semicolon as delimiter
# add sep and encoding parameters when reading the csv file
icd10who = pd.read_csv(
    'input/icd10WHO/icd102019syst_codes_WHO.txt',
    header=None,
    sep=';',           # semicolon delimiter
    encoding='utf-8'   # adjust encoding type if you encounter issues
)


# Dispays rows and column information of the dataframe
icd10who.info()

# Displays the first 5 rows of the dataframe
print(icd10who.head())

# Base on the result above we can see that the coloumns have default names 0,1,2,3, etc
# we can rename those numbers to a more meaningful name
icd10who = icd10who.rename(columns = {
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

print(icd10who.head())
icd10who.info()
### Selecting columns of interest and adding to a new dataframe
shorticd10who = icd10who[['Code3', 'Description']]

# adding a new column to the new dataframe with a default value
shorticd10who ['last_updated'] = '09-05-2025'

# renaming column names from shortlist
shorticd10who = shorticd10who.rename(columns={
        'Code3': 'Code'
})

shorticd10who

save_to_csv(shorticd10who, 'icd10who_short.csv')