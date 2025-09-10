import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.common_functions import save_to_format


file_path = 'input/icd102019syst_codes.txt'

columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

df = pd.read_csv(file_path, sep=';', header=None, names=columns)

df_col = ['code', 'detailed_title']

df_small = df[['code', 'detailed_title']]

df_small = df[df_col]

for col in ['code', 'detailed_title']:
    df_small[col] = df_small[col].astype(str).str.strip()        # remove leading spaces after words
    df_small[col] = df_small[col].str.replace(r'\s+', ' ', regex=True)  #remove extra spacing between words

#missing + null values
df_small = df_small.replace({'': None, 'nan': None, 'NaN': None})
df_small = df_small.dropna(subset=['code', 'detailed_title']) #now there is no empty description/codes

df_small = df_small.drop_duplicates(subset=['code'])

df_small['last_updated'] = '09-10-2025'

print(df_small.head())

save_to_format(df_small, baseFile="icd102019syst_codes")
# output_path = 'assignment1/medical-codex-pipeline/output/icd102019syst_codes.csv'
# df.to_csv(output_path, index=False)

print(f"Successfully parsed {len(df)} records from {file_path}")
print(f"\nFirst 5 rows:")
print(df.head())
