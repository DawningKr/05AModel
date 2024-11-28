from typing import List
import numpy as np
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
