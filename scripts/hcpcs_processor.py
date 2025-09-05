import pandas as pd
from utils.common_functions import save_to_csv
# Loading Data Set and have it as a variable
hcpc_df = pd.read_csv('input/hcpc/HCPC2025_OCT_ANWEB.csv')

# removing whitespaces from column names
hcpc_df.columns = hcpc_df.columns.str.strip()


# Dispays rows and column information of the dataframe
hcpc_df.info()

# Displays the first 5 rows of the dataframe
print(hcpc_df.head())

# Column Exploration and checking potential columns to be used
## Displays the column information of the dataframe
### If your dataframe has spaces headers, you can access them by using brackets []
hcpc_df.HCPC
hcpc_df['LONG DESCRIPTION']
hcpc_df['SHORT DESCRIPTION']

### Selecting columns of interest and adding to a new dataframe
shorthcpc = hcpc_df[['HCPC', 'LONG DESCRIPTION']]

# adding a new column to the new dataframe with a default value
shorthcpc ['last_updated'] = '09-05-2025'

# renaming column names from shortlist
shorthcpc = shorthcpc.rename(columns={
    'HCPC': 'Code',
    'LONG DESCRIPTION': 'Description'
})

shorthcpc

save_to_csv(shorthcpc,'hcpc_short.csv')