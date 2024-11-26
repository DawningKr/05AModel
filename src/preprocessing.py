import pandas as pd
import os

from utils import get_file_paths

T = 7

def max_min_normalize(file_location: str, output_location: str) -> None:
    file_paths = get_file_paths(file_location)
    output_paths = get_file_paths(output_location)
    for index, file_path in enumerate(file_paths):
        df = pd.read_csv(file_path)
        for key in df.columns.to_list()[3:7]:
            df[key] = df[key].astype(float)
            min_value = df[key].min()
            max_value = df[key].max()
            if key == 'pH*':
                df[key] = df[key].map(lambda x: 1 - abs(x - T) / max(abs(x - min_value), abs(x - max_value)))
            elif key == 'DO':
                df[key] = df[key].map(lambda x: (x - min_value) / (max_value - min_value))
            else:
                df[key] = df[key].map(lambda x: (max_value - x) / (max_value - min_value))
        df.to_csv(output_paths[index])


if __name__ == '__main__':
    file_location = "data/raw/WaterQuality/"
    output_location = "data/processed/MaxMinNormalized/"
    max_min_normalize(file_location, output_location)
