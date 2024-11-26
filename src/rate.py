import numpy as np
import pandas as pd
import os

from utils import get_file_paths

file_location = "data/processed/MaxMinNormalized/"
output_location = "data/processed/NormalizedWithScore/"

file_paths = get_file_paths(file_location)
output_paths = get_file_paths(output_location)

for index, file_path in enumerate(file_paths):
    df = pd.read_csv(file_path)
    weights = []

    for column in df.columns.to_list()[4:8]:
        df[column] = df[column].astype(float)
        total_value = df[column].sum()
        k = np.log(len(df[column]))
        df[column] = df[column].map(lambda x: x / total_value)
        values = df[column].values
        e = -k * np.sum(values * np.log(values, where=values > 0))
        weights.append(1 - e)

    total_value = sum(weights)
    weights = list(map(lambda x: x / total_value, weights))

    df['score'] = weights[0] * df['pH*'] + weights[1] * df['DO'] + weights[2] * df['CODMn'] + weights[3] * df['NH3-N']
    df.to_csv(output_paths[index])
