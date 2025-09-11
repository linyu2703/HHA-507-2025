import pandas as pd 
import os
import sys

# allowing python to import funcs from parent directory util folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.common_functions import save_to_format

# importing the loinc csv file using pandas read_csv func
loinc = pd.read_csv('input/Loinc.csv')

# getting the general description of the column names, data type
# getting unqiue values in status column and printing the first row of the dataset uisng iloc func
loinc.info() 
loinc.STATUS.value_counts()
loinc.iloc[0]

# this allows to view loinc_num and long_common_name columns frm the general loinc dataframe
loinc.LOINC_NUM
loinc.LONG_COMMON_NAME

# creating a smaller loinc dataframe of just loinc_num and long_common_name
list_cols = ['LOINC_NUM', 'LONG_COMMON_NAME']

loinc_small = loinc[['LOINC_NUM', 'LONG_COMMON_NAME']]
loinc_small = loinc[list_cols]

# appending a new column with last updated date
loinc_small['last_updated'] = '09-10-2025'

# renaming the column headers to code and description
loinc_small = loinc_small.rename(columns={
    'LOINC_NUM': 'code',
    'LONG_COMMON_NAME': 'description',
})

# using the called save_to_format function to change the df_small dataframe, to a csv in output folder
save_to_format(loinc_small, baseFile="loinc_small")
