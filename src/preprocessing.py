import pandas as pd
import os

T = 7

def max_min_normalize(file_location: str, output_location: str) -> None:
    for file_name in os.listdir(file_location):
        file_path = os.path.join(file_location, file_name)
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
        output_path = os.path.join(output_location, file_name)
        df.to_csv(output_path)


if __name__ == '__main__':
    file_location = "data/raw/WaterQuality/"
    output_location = "data/processed/MaxMinNormalized/"
    max_min_normalize(file_location, output_location)
