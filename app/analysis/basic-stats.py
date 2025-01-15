import pandas as pd
import os
from datetime import date
import schemas as sch
import globals as cfg

today = date.today()
ts = today.strftime("%Y%m%d")

dataset_code = 'all'
datasets = cfg.get_datasets(dataset_code)

shape_dict = {}
for dataset in datasets:
    archive_code = dataset
    print(archive_code)
    root_dir = cfg.get_project_root()

    source_file = str(root_dir) + '/source-data/' + archive_code + '/verbatim.txt'
    df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8', encoding_errors='ignore', on_bad_lines='skip', dtype=object)
    shape_dict[archive_code] = df.shape
    #print(df.shape)

print(shape_dict)
