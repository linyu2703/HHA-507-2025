import pandas as pd

# path to the HCPCS text file
file_path = "assignment1/medical-codex-pipeline/input/HCPC2025_OCT_ANWEB_v3.txt"

# colspecs based on actual column widths
colspecs = [(0, 11), (11, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
column_names = [
    "Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"
]

#reading using fwf
df = pd.read_fwf(file_path, colspecs=colspecs, names=column_names, dtype=str)

#starting cap for each str in descrip
df['Description1'] = df['Description1'].astype(str).str.capitalize()

df_cols = ['Code', 'Description1']

df_small = df[['Code', 'Description1']]
df_small = df[df_cols]

df_small = df_small.rename(columns={'Code': 'code', 'Description1': 'description'})

#trimming
for col in ['code', 'description']:
    df_small[col] = df_small[col].astype(str).str.strip()        # remove leading spaces after words
    df_small[col] = df_small[col].str.replace(r'\s+', ' ', regex=True)  #remove extra spacing between words

#missing + null values
df_small = df_small.replace({'': None, 'nan': None, 'NaN': None})
df_small = df_small.dropna(subset=['code', 'description']) #now there is no empty description/codes

df_small = df_small.drop_duplicates(subset=['code'])

df_small['last_updated'] = '2025-09-03'

print(df_small.head())

## saving csv into output subfolder
output_path = "assignment1/medical-codex-pipeline/output/HCPC2025_OCT_ANWEB.csv"
df_small.to_csv(output_path, index=False)