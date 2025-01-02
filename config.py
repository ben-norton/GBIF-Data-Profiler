import os
from datetime import date
from pathlib import Path

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

def get_project_root() -> Path:
    return os.path.dirname(os.path.abspath(__file__))

def get_data_root() -> Path:
    return Path(get_project_root(), "data")

source_datasets = [
    "0049391-241126133413365/occurrence.txt",
    "0049394-241126133413365/occurrence.txt",
    "0049395-241126133413365/occurrence.txt",
    "0051851-241126133413365/occurrence.txt",
]

def get_today():
    today = date.today()
    ts = today.strftime("%Y%m%d")
    return ts
