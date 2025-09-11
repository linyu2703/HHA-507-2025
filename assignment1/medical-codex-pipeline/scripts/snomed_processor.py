import polars as pl
from pathlib import Path
import os
import sys

# allowing python to import funcs from parent directory util folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.common_functions import save_to_format

# importing the pathway to the snomed txt file
file_path = Path('input/sct2_Description_Full-en_US1000124_20250301.txt')

#reads and loads snomed with delimiter of '\t', assigning dtypes to column headers
df = pl.read_csv(
    file_path,
    separator='\t',
    has_header=True,
    quote_char=None,
    encoding='utf8-lossy',
    truncate_ragged_lines=True, # rows with missing values are handled
    dtypes={
        'id': pl.Utf8,
        'effectiveTime': pl.Utf8,
        'active': pl.Int32,
        'moduleId': pl.Utf8,
        'conceptId': pl.Utf8,
        'languageCode': pl.Utf8,
        'typeId': pl.Utf8,
        'term': pl.Utf8,
        'caseSignificanceId': pl.Utf8
    }
)
# renaming conceptId and term columns to code and description, respectively
# df_small variable is used to create a smaller sample dataframe of just code and description columns
df_col = ['conceptId', 'term']

df_small = df[['conceptId', 'term']]
df_small = df[df_col]
df_small = df_small.rename({'conceptId': 'code', 'term': 'description'})

print(df_small.head()) # seeing if it worked by displaying first 5 rows

# strip_chars just removes the leading/trailing whitespaces
# replace_all the multiple spacing with just a single spacing within description
df_small["description"].str.strip_chars().str.replace_all(r"\s+", " ").alias("description")

# keeping only unique code values, which essentially eliminates potential duplicate codes
df_small = df_small.unique(subset=['code'])

# appending a new column to df_small that gives the last updated date
df_small = df_small.with_columns([
    pl.lit("09-10-2025").alias("last_updated")
])

print(df_small.head()) # again checking if everything worked out and new column is added

save_to_format(df_small, baseFile="sct2_Description_Full") # using the called save_to_format function to change the df_small dataframe, to a csv in output folder


print(f"Successfully parsed {len(df)} records from SNOMED CT file")
print(f"Dataset shape: {df.shape}")
print(f"\nColumn names: {df.columns}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")
print(f"\nActive terms count: {df.filter(pl.col('active') == 1).height}")
print(f"Language codes: {df['languageCode'].unique().to_list()}")