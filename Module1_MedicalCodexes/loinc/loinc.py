import pandas as pd 

## Input/Loinc.csv
loinc = pd.read_csv('Module1_MedicalCodexes/loinc/Loinc.csv')

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

file_output_path = 'Module1_MedicalCodexes/loinc/output/loinc_small.csv'

loinc_small.to_csv('Module1_MedicalCodexes/loinc/output/loinc_small.csv')

loinc_small.to_csv('Module1_MedicalCodexes/loinc/output/loinc_small_noindex.csv', index=False)