from typing import List
import os

def get_file_paths(directory_path: str) -> List[str]:
    file_paths = []
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        file_paths.append(file_path)
    return file_paths

