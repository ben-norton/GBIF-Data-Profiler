import globals as cfg
import pandas as pd
from pathlib import Path

# Check if multimedia records exist
ts = cfg.get_today()
root_dir = cfg.get_project_root()
media_dir = cfg.get_media_directory()
dataset_code = 'all'        # Dataset Filter. See globals.py

datasets = cfg.get_datasets(dataset_code)
media_dict = {}

for dataset in datasets:
    package_id = dataset
    print(package_id)
    source_file = Path(str(root_dir) + '/source-data/' + package_id + '/multimedia.txt')
    if source_file.is_file():
        df_package_media = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8', encoding_errors='ignore',dtype=object)
        df_package_dict = {}
        df_package_dict['length'] = len(df_package_media)
        df_package_dict['shape'] = df_package_media.shape
        df_package_dict['rows'] = df_package_media.shape[0]
        df_package_dict['columns'] = df_package_media.shape[1]
        df_package_dict['timestamp'] = ts
        media_dict[package_id] = df_package_dict

df_meta_dict = pd.DataFrame.from_dict(media_dict, orient='index')
md_file = 'scan-media-results.md'
md = df_meta_dict.to_markdown()
with open(md_file, 'w') as f:
    f.write(md)
