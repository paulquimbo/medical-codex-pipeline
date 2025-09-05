import pandas as pd

# Define your reusable path
CSV_PATH = 'output/csv/'

def save_to_csv(df, filename):
  
    df.to_csv(CSV_PATH + filename, index=False)
