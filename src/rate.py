import numpy as np
import pandas as pd
import os

file_location = "data/processed/MaxMinNormalized/"
output_location = "data/processed/NormalizedWithScore/"

for file_name in os.listdir(file_location):
    file_path = os.path.join(file_location, file_name)
    output_path = os.path.join(output_location, file_name)
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
    df.to_csv(output_path)
