import pandas as pd
import os
import polars as pl

def save_to_format(df:pd.DataFrame, baseFile: str, outputDir: str='output') -> None:
    if not os.path.exists(outputDir):
        os.makedirs(outputDir,exist_ok=True)
    csv_path = os.path.join(outputDir, f"{baseFile}.csv")

    if isinstance(df, pd.DataFrame):
        df.to_csv(csv_path, index = False)
    else:
        df.write_csv(csv_path)
   
