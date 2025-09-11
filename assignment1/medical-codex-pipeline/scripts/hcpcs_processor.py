import pandas as pd
import os
import sys

# allowing python to import funcs from parent directory util folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.common_functions import save_to_format

# path to the HCPCS text file
file_path = "input/HCPC2025_OCT_ANWEB_v3.txt"

# colspecs based on actual column widths
colspecs = [(0, 11), (11, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
column_names = [
    "Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"
]

# reading and loading data using fwf into df
df = pd.read_fwf(file_path, colspecs=colspecs, names=column_names, dtype=str)

# starting capitlization for each str in description
df['Description1'] = df['Description1'].astype(str).str.capitalize()

# creating a smaller dataframe of just code and descrpition in df_small
# renaming code and descrption1 to appropriate column headers
df_cols = ['Code', 'Description1']

df_small = df[['Code', 'Description1']]
df_small = df[df_cols]
df_small = df_small.rename(columns={'Code': 'code', 'Description1': 'description'})

# converts both columns to str type and removes extra whitespaces and leading spaces after and between words
for col in ['code', 'description']:
    df_small[col] = df_small[col].astype(str).str.strip()  
    df_small[col] = df_small[col].str.replace(r'\s+', ' ', regex=True) 

# replacing blank, nan, NaN strings with none
# dropping rows that are empty without description or codes and dropping duplicate codes
df_small = df_small.replace({'': None, 'nan': None, 'NaN': None})
df_small = df_small.dropna(subset=['code', 'description']) #now there is no empty description/codes
df_small = df_small.drop_duplicates(subset=['code'])

# appending new column for last updated date
df_small['last_updated'] = '09-10-2025'

print(df_small.head()) #printing first 5 rows of df_small

# using the called save_to_format function to change the df_small dataframe, to a csv in output folder
save_to_format(df_small, baseFile="HCPC2025_OCT_ANWEB")
