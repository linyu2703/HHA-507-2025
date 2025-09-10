import polars as pl
from pathlib import Path
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.common_functions import save_to_format

#need to fix + change directory

# https://www.nlm.nih.gov/research/umls/rxnorm/docs/techdoc.html#s12_10

file_path = Path('input/RXNATOMARCHIVE.RRF')

columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]

df = pl.read_csv(
    file_path,
    separator='|',
    has_header=False,
    new_columns=columns,
    truncate_ragged_lines=True
)

df_col = ['code', 'str']

df_small = df[['code', 'str']]

df_small = df[df_col]

df_small = df_small.rename({'str': 'description'})


#trimming
df_small["description"].str.strip_chars().str.replace_all(r"\s+", " ").alias("description")


# #missing + null values
# df_small = df_small.replace({'': None, 'nan': None, 'NaN': None}).alias(df_small)
# df_small = df_small.dropna(subset=['code', 'description']) #now there is no empty description/codes

df_small = df_small.unique(subset=['code'])

df_small = df_small.with_columns([
    pl.lit("09-10-2025").alias("last_updated")
])

print(df_small.head())

save_to_format(df_small, baseFile="RXNATOMARCHIVE")

# output_dir = Path('Module1_MedicalCodexes/rxnorm/output')
# output_dir.mkdir(exist_ok=True)
# output_path = output_dir / 'RXNATOMARCHIVE.csv'

# df.write_csv(output_path)

print(f"Successfully parsed {len(df)} records from RXNATOMARCHIVE.RRF")
print(f"Dataset shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")