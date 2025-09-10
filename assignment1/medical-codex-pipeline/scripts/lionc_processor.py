import pandas as pd 
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.common_functions import save_to_format

## Input/Loinc.csv
loinc = pd.read_csv('input/Loinc.csv')

### Info to describe 
loinc.info()

### Strings 
loinc.STATUS.value_counts()

### print first row
loinc.iloc[0]

#### Check potential column names that we think we want to keep: LOINC_NUM, DefinitionDescription
loinc.LOINC_NUM
loinc.LONG_COMMON_NAME

list_cols = ['LOINC_NUM', 'LONG_COMMON_NAME']

loinc_small = loinc[['LOINC_NUM', 'LONG_COMMON_NAME']]
loinc_small = loinc[list_cols]

loinc_small['last_updated'] = '2025-09-03'

# loinc_small = loinc_small.rename(columns={})

loinc_small = loinc_small.rename(columns={
    'LOINC_NUM': 'code',
    'LONG_COMMON_NAME': 'description',
})

save_to_format(loinc_small, baseFile="loinc_small")

# file_output_path = 'assignment1/medical-codex-pipeline/output/loinc_small.csv'

# loinc_small.to_csv(file_output_path)

# loinc_small.to_csv('assignment1/medical-codex-pipeline/output/loinc_small_noindex.csv', index=False)