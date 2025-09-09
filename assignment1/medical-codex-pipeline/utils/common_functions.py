import pandas as pd
import os

def save_to_format(df:pd.DataFrame, baseFile: str, outputDir: str='assignment1/medical-codex-pipeline/output') -> None:
    os.makedirs(outputDir,exist_ok=True)
    csv_path = os.path.join(outputDir, f'{baseFile}.csv')
    df.to_csv(csv_path, index = False)
