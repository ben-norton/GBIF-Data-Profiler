import os
from datetime import date
from pathlib import Path

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

def get_media_directory() -> Path:
    return Path('H:/media')

def get_project_root() -> Path:
    return os.path.dirname(os.path.abspath(__file__))

def get_data_root() -> Path:
    return Path(get_project_root(), "data")

# Get Datasets partitioned from full datasets (see meta.yml)
# Datasets commented out were successfully parsed by sweetviz
def get_datasets(str):
    if(str == 'usnm'):
        datasets = [
            '0049391-241126133413365',
            '0049394-241126133413365',
            '0052484-241126133413365',
            '0052487-241126133413365',
            '0052489-241126133413365',
            '0054884-241126133413365',
            '0002610-250325103851331',
            '0054921-241126133413365',
            '0055081-241126133413365'
        ]
    elif(str == 'naturalis'):
        datasets = [
            '0061686-241126133413365',
            '0061690-241126133413365'
        ]
    elif (str == 'ypm'):
        datasets = [
            '0061682-241126133413365',
            '0061684-241126133413365',
            '0000644-250214102907787'
        ]
    elif (str == 'fmnh'):
        datasets = [
            '0000214-250121130708018',
            '0002582-250127130748423',
            '0011504-250127130748423'
        ]
    elif (str == 'flmnh'):
        datasets = [
            '0000647-250214102907787'
        ]
    elif (str == 'rgbe'):
        datasets = [
            '0000320-250213122211068'
        ]
    elif (str == 'ncsm'):
        datasets = [
            '0001383-250121130708018',
        ]
    elif (str == 'cumv'):
        datasets = [
            '0000571-250121130708018',
        ]
    elif (str == 'cm'):
        datasets = [
            '0000014-250226211518916',
        ]
    elif (str == 'br'):
        datasets = [
            '0007170-250310093411724',
        ]
    elif (str == 'all'):
        datasets = [
            '0000214-250121130708018',
            '0000571-250121130708018',
            '0001383-250121130708018',
            '0002582-250127130748423',
            '0011504-250127130748423',
            '0049391-241126133413365',
            '0049394-241126133413365',
            '0049395-241126133413365',
            '0052484-241126133413365',
            '0052487-241126133413365',
            '0052489-241126133413365',
            '0054884-241126133413365',
            '0054887-241126133413365',
            '0054921-241126133413365',
            '0055081-241126133413365',
            '0061682-241126133413365',
            '0061684-241126133413365',
            '0061686-241126133413365',
            '0061690-241126133413365',
            '0000320-250213122211068'
        ]
    elif (str == 'media'):
        datasets = [
            '0011504-250127130748423'
        ]
    elif (str == 'fix'):
        datasets = [
            '0002610-250325103851331'
        ]

    else:
        datasets = []

    return datasets

# Subset of Datasets for specific purposes
def get_target_datasets():
    datasets = [
        '0049391-241126133413365'
    ]
    return datasets

def get_today():
    today = date.today()
    ts = today.strftime("%Y%m%d")
    return ts
