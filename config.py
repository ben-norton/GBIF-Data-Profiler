import os
from pathlib import Path

def get_project_root() -> Path:
    return os.path.dirname(os.path.abspath(__file__))

def get_data_root() -> Path:
    return Path(get_project_root(), "data")
