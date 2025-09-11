import pandas as pd
import os

# save_to_format function that takes in parameters df, baseFile, outputDir
# df by default should be in pandas dataframe, baseFile is the file name in a string type, outputDir directs the output directory to output folder, and function returns nothing and just saves the file
def save_to_format(df:pd.DataFrame, baseFile: str, outputDir: str='output') -> None:
    if not os.path.exists(outputDir): # checking if the already directory exists, if not then it creates it
        os.makedirs(outputDir,exist_ok=True)
    csv_path = os.path.join(outputDir, f"{baseFile}.csv") # joins the outputDir and baseFile name into a valid path

    if isinstance(df, pd.DataFrame): # if the default datafram is a pandas dataframe then it converts using pandas' to_csv 
        df.to_csv(csv_path, index = False)
    else:
        df.write_csv(csv_path) # otherwise if it is in polars dataframe then it uses the write_csv
   
