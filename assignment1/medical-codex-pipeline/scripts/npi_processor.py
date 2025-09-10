import polars as pl
import pandas as pd
import time
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.common_functions import save_to_format

npi_file_path = 'input/npidata_pfile_20050523-20250907.csv'

## --- Polars load ---
start_time_polars = time.time()
df_polars = pl.read_csv(npi_file_path, n_rows=1000)  # limit for testing
end_time_polars = time.time()
elapsed_time_polars = end_time_polars - start_time_polars
print(f"Polars load time: {elapsed_time_polars:.2f} sec")

## --- Pandas load ---
start_time_pandas = time.time()
df_pandas = pd.read_csv(npi_file_path, nrows=1000, low_memory=False)
end_time_pandas = time.time()
elapsed_time_pandas = end_time_pandas - start_time_pandas
print(f"Pandas load time: {elapsed_time_pandas:.2f} sec")

## --- Basic info ---
print(f"\nSuccessfully loaded {len(df_polars)} records from NPI data")
print(f"Columns: {df_polars.columns}")
print(f"Dataset shape: {df_polars.shape}")
print(df_polars.head())

print(f"\nMemory usage (MB): {df_polars.estimated_size() / 1024**2:.2f}")

## --- Select smaller dataset ---
df_polars_small = df_polars.select([
    'NPI',
    'Provider Last Name (Legal Name)'  # adjust if spelling differs
])

## add last_updated column
df_polars_small = df_polars_small.with_columns(
    pl.lit('09-10-2025').alias('last_updated')
)

## rename columns
df_polars_small = df_polars_small.rename({
    'NPI': 'code',
    'Provider Last Name (Legal Name)': 'description'
})

## save to output
save_to_format(df_polars_small.to_pandas(), baseFile="npi_small")
# df_polars_small.write_csv('assignment1/medical-codex-pipeline/output/npi_small.csv')
# df_polars_small.write_parquet('assignment1/medical-codex-pipeline/output/npi_small.parquet')
