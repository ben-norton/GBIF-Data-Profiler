import pandas as pd
import config as cfg
import os
from datetime import date

today = date.today()
ts = today.strftime("%Y%m%d")

datasets = cfg.get_all_datasets()

shape_dict = {}
for dataset in datasets:
    archive_code = dataset
    print(archive_code)
    root_dir = cfg.get_project_root()

    source_file = str(root_dir) + '/source-data/' + archive_code + '/occurrence.txt'
    df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8')
    print(df.shape)
