import globals as cfg
import pandas as pd

# Check if multimedia records exist

root_dir = cfg.get_project_root()
media_dir = cfg.get_media_directory()
dataset_code = 'all'        # Dataset Filter. See globals.py

datasets = cfg.get_datasets(dataset_code)
media_dict = {}

for dataset in datasets:
    package_id = dataset
    print(package_id)
    source_file = str(root_dir) + '/source-data/' + package_id + '/multimedia.txt'
    df_package_media = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8', encoding_errors='ignore',dtype=object)
    df_package_dict = {}
    df_package_dict['length'] = len(df_package_media)
    df_package_dict['shape'] = df_package_media.shape
    media_dict[package_id] = df_package_dict

df_meta_dict = pd.DataFrame.from_dict(media_dict, orient='index')
md_file = 'media_profiles.md'
md = df_meta_dict.to_markdown()
with open(md_file, 'w') as f:
    f.write(md)
