from typing import List
import numpy as np
import pandas as pd
import os

def get_file_paths(directory_path: str) -> List[str]:
    file_paths = []
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        file_paths.append(file_path)
    return file_paths

def mean(*args) -> float:
    return sum(args) / len(args)

def get_alpha(distance, water_speed, K=0.2):
    return np.exp(-K * distance * 1000 / water_speed)

def calculate_pollution_flow(pre_pollution, local_pollution, water_flow, alpha):
    upstream_pollution = pre_pollution * alpha
    return local_pollution * water_flow / 1000 + upstream_pollution

def row_sort(data_df: pd.DataFrame) -> pd.DataFrame:
    tag = data_df.columns[0]
    
    years = data_df[tag].to_numpy()
    locations = data_df.columns[1:].to_numpy()
    
    columns = [tag] + [f"Rank_{i}" for i in range(1, len(data_df.columns))]
    output_df = pd.DataFrame(columns=columns)

    for index, row in data_df.iterrows():
        pollution_score = row[1:].astype(float).to_list()
        sorted_index = np.argsort(pollution_score)[::-1]
        sorted_row = np.hstack([years[index], locations[sorted_index]])
        output_df.loc[index] = sorted_row

    return output_df
