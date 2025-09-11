import pandas as pd
import os
import sys

# allowing python to import funcs from parent directory util folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.common_functions import save_to_format

# reading the raw txt file and assigning it to file_path var
file_path = 'input/icd102019syst_codes.txt'

# no header exist in data so creating new column headers
columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

# reading using pandas with the delimiter of ';'
df = pd.read_csv(file_path, sep=';', header=None, names=columns)

# creating a smaller dataframe of code and detailed_title assigned to df_small
df_col = ['code', 'detailed_title']
df_small = df[['code', 'detailed_title']]
df_small = df[df_col]

# renaming detailed_title to description
df_small = df_small.rename(columns={'detailed_title': 'description'})

# converts both columns to str type and removes extra whitespaces and leading spaces after and between words
for col in ['code', 'description']:
    df_small[col] = df_small[col].astype(str).str.strip()    
    df_small[col] = df_small[col].str.replace(r'\s+', ' ', regex=True)  

# replace blank stirngs and nan and NaN values with none
# dropping rows with missing code or description, and removing duplicate codes
df_small = df_small.replace({'': None, 'nan': None, 'NaN': None})
df_small = df_small.dropna(subset=['code', 'description']) #now there is no empty description/codes
df_small = df_small.drop_duplicates(subset=['code'])

# adding a new column for last updated date
df_small['last_updated'] = '09-10-2025'

print(df_small.head()) # checking first 5 rows of df_small to check if everthing worked

# using the called save_to_format function to change the df_small dataframe, to a csv in output folder
save_to_format(df_small, baseFile="icd102019syst_codes")

print(f"Successfully parsed {len(df)} records from {file_path}")
print(f"\nFirst 5 rows:")
print(df.head())
