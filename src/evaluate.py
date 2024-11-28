import numpy as np
import pandas as pd

from utils import get_file_paths

file_location = "data/processed/NormalizedWithScore/"
output_path = "data/result/ScoreEvaluation.csv"

file_paths = get_file_paths(file_location)

# We got 17 places in total
result = np.zeros(17)
locations = None

for file_path in file_paths:
    df = pd.read_csv(file_path)
    result += df['score']
    if locations is None:
        locations = df['点位名称']

# add statistical meaning to the result -> average score per month
result /= 24
index_order = result.argsort()[::-1]
locations = locations[index_order]
locations.reset_index(drop=True, inplace=True)
locations.to_csv(output_path)