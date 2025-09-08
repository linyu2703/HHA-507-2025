import pandas as pd

icd10 = pd.read_csv('/Users/yulin/Documents/python/HHA-507-2025/assignment1/icd10cm/icd10cm_order_2025.txt', sep = "\t")

print(icd10.head())