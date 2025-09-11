import polars as pl
import pandas as pd
import time
import os
import sys

# allowing python to import funcs from parent directory util folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.common_functions import save_to_format

# assigning npi_file_path var to load the npi csv file
npi_file_path = 'input/npidata_pfile_20050523-20250907.csv'

# reads using polars, only the first 1000 rows and seeing how long it takes to load it
start_time_polars = time.time()
df_polars = pl.read_csv(npi_file_path, n_rows=1000)
end_time_polars = time.time()
elapsed_time_polars = end_time_polars - start_time_polars
print(f"Polars load time: {elapsed_time_polars:.2f} sec")

# reading using pandas, only the first 1000 rows and seeing how long it takes to load
start_time_pandas = time.time()
df_pandas = pd.read_csv(npi_file_path, nrows=1000, low_memory=False)
end_time_pandas = time.time()
elapsed_time_pandas = end_time_pandas - start_time_pandas
print(f"Pandas load time: {elapsed_time_pandas:.2f} sec")

# prints column names, shape (row by col), and first 5 rows
print(f"\nSuccessfully loaded {len(df_polars)} records from NPI data")
print(f"Columns: {df_polars.columns}")
print(f"Dataset shape: {df_polars.shape}")
print(df_polars.head())
print(f"\nMemory usage (MB): {df_polars.estimated_size() / 1024**2:.2f}")

# creating a smaller datafram using polars of the npi and providers last name
df_polars_small = df_polars.select([
    'NPI',
    'Provider Last Name (Legal Name)'  
])

# add a constant column that gives the date of last update
df_polars_small = df_polars_small.with_columns(
    pl.lit('09-10-2025').alias('last_updated')
)

# renmaing headers npi to code and provider last name of description
df_polars_small = df_polars_small.rename({
    'NPI': 'code',
    'Provider Last Name (Legal Name)': 'description'
})

# using the called save_to_format function to change the df_polars_small dataframe, to a csv in output folder
save_to_format(df_polars_small.to_pandas(), baseFile="npi_small")

