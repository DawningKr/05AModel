import numpy as np
import pandas as pd

from utils import row_sort

CODMn_result = pd.read_csv('data/result/CODMnResult.csv')
NH3N_result = pd.read_csv('data/result/NH3NResult.csv')

CODMn_sorted = row_sort(CODMn_result)
NH3N_sorted = row_sort(NH3N_result)

CODMn_sorted.to_csv("data/result/CODMnSorted.csv")
NH3N_sorted.to_csv("data/result/NH3N_sorted.csv")