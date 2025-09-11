import polars as pl
from pathlib import Path
import os
import sys

# allowing python to import funcs from parent directory util folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.common_functions import save_to_format

# importing the pathway to the rxnorm rrf file
file_path = Path('input/RXNATOMARCHIVE.RRF')

# since rrf file doesnt have headers, we just assign them the following headers
columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]

# reading the data with the delimiter of '|' with no header row
df = pl.read_csv(
    file_path,
    separator='|',
    has_header=False,
    new_columns=columns,
    truncate_ragged_lines=True # rows with missing values are handled
)

df_col = ['code', 'str']

# creating a smaller dataframe of just code and str and renaming the str column to description
df_small = df[['code', 'str']]
df_small = df[df_col]
df_small = df_small.rename({'str': 'description'})


# strip_chars just removes the leading/trailing whitespaces
# replace_all the multiple spacing with just a single spacing within description
df_small["description"].str.strip_chars().str.replace_all(r"\s+", " ").alias("description")

# keeping only unique code values, which essentially eliminates potential duplicate codes
df_small = df_small.unique(subset=['code'])

# appending a new column to df_small that gives the last updated date
df_small = df_small.with_columns([
    pl.lit("09-10-2025").alias("last_updated")
])

print(df_small.head()) #checking df_small dataframe to see if everything worked out and appended

# using the called save_to_format function to change the df_small dataframe, to a csv in output folder
save_to_format(df_small, baseFile="RXNATOMARCHIVE")

print(f"Successfully parsed {len(df)} records from RXNATOMARCHIVE.RRF")
print(f"Dataset shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")