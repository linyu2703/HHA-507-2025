import polars as pl
from pathlib import Path
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.common_functions import save_to_format


file_path = Path('input/sct2_Description_Full-en_US1000124_20250301.txt')

df = pl.read_csv(
    file_path,
    separator='\t',
    has_header=True,
    quote_char=None,
    encoding='utf8-lossy',
    truncate_ragged_lines=True,
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

df_col = ['conceptId', 'term']

df_small = df[['conceptId', 'term']]

df_small = df[df_col]

df_small = df_small.rename({'conceptId': 'code', 'term': 'description'})

print(df_small.head())

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

save_to_format(df_small, baseFile="sct2_Description_Full")

# output_dir = Path('Module1_MedicalCodexes/snowmed/output')
# output_dir.mkdir(exist_ok=True)
# output_path = output_dir / 'sct2_Description_Full.csv'

# df.write_csv(output_path)

print(f"Successfully parsed {len(df)} records from SNOMED CT file")
print(f"Dataset shape: {df.shape}")
print(f"\nColumn names: {df.columns}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")

print(f"\nActive terms count: {df.filter(pl.col('active') == 1).height}")
print(f"Language codes: {df['languageCode'].unique().to_list()}")