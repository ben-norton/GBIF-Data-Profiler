import os
from datetime import date
from pathlib import Path

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

def get_project_root() -> Path:
    return os.path.dirname(os.path.abspath(__file__))

def get_data_root() -> Path:
    return Path(get_project_root(), "data")

# Get Datasets partitioned from full datasets (see meta.yml)
# Datasets commented out were successfully parsed by sweetviz
def get_datasets():
    datasets = [
#        '0052484-241126133413365',
#        '0052487-241126133413365',
        '0052489-241126133413365',
        '0054884-241126133413365',
        '0054887-241126133413365',
        '0054921-241126133413365',
        '0055081-241126133413365'
    ]
    return datasets

# Get Full Datasets (without paarameter-based partitioning
def get_full_datasets():
    full_datasets = [
#        '0049391-241126133413365',
        '0049394-241126133413365',
#        '0049395-241126133413365'
    ]
    return full_datasets

def get_all_datasets():
    all_datasets = [
        '0049391-241126133413365',
        '0049394-241126133413365',
        '0049395-241126133413365',
        '0051851-241126133413365',
        '0052484-241126133413365',
        '0052487-241126133413365',
        '0052489-241126133413365',
        '0054884-241126133413365',
        '0054887-241126133413365',
        '0054921-241126133413365',
        '0055081-241126133413365'
    ]
    return all_datasets

# Subset of Datasets for testing purposes
def get_test_datasets():
    datasets = [
        '0055081-241126133413365'
    ]
    return datasets


def get_today():
    today = date.today()
    ts = today.strftime("%Y%m%d")
    return ts
