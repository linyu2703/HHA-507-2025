import polars as pl

npi_file_path = 'Module1_MedicalCodexes/npi/npidata_pfile_20050523-20250810.csv'

## just load the first 1000 rows
df = pl.read_csv(npi_file_path, n_rows=1000)

print(f"Successfully loaded {len(df)} records from NPI data")
print(f"Columns: {df.columns}")
print(f"\nDataset shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())

print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")

## save to CSV
output_path = 'Module1_MedicalCodexes/npi/output/npidata_pfile_20050523-20250810.csv'
df.write_csv(output_path)
