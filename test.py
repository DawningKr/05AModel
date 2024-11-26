import pandas as pd
import numpy as np
import os

file_location = "data/processed/NormalizedWithScore/"
for file_name in os.listdir(file_location):
    file_path = os.path.join(file_location, file_name)
    df = pd.read_csv(file_path)