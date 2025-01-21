import os
import re
import datetime
import shutil
import globals as cfg
import pathlib
from pathlib import Path
import pandas as pd
import glob
import yaml
import vars as pvars

# Generate Web Source Data

def generate_web_sources(target, source):

    # Create dataframe from dataset profiles
    master_list = list()
    for name in os.listdir(target):
        pathname = os.path.join(target, name)
        data_dict = {}
        if os.path.isfile(pathname):
            path = pathlib.Path(pathname)
            mtime = path.stat().st_mtime
            last_modified = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M')
            if name.endswith('.html'):
                data_dict['profile_link'] = 'components/dataset-profiles/' + name
                data_dict['last_modified'] = last_modified
                data_dict['package_id'] = re.search(r"\d{7}-\d{15}", name).group()
                # Split filename by hyphen and remove extension
                name_split = path.stem.split("-")
                # Get Institution Code and add to Dict
                data_dict['source_file'] = name_split[3] + '.txt'
                data_dict['institution_code'] = name_split[4]
                # Get Profiler Library and add to Dict
                profiler_notation = name_split[5]
                if (profiler_notation == 'yd'):
                    profiler = 'YData'
                elif (profiler_notation == 'sv'):
                    profiler = 'Sweetviz'
                else:
                    profiler = 'Unknown'
                data_dict['profile_library'] = profiler
                master_list.append(data_dict)

    df_profiles = pd.DataFrame.from_dict(master_list)
    print(df_profiles.columns)

    # Create meta.yml dataframe from meta.yml files in source-datasets directory
    yml_dict = []
    for yf in glob.glob(source + '/**/meta.yml', recursive=True):
        with open(yf, 'r') as f:
            meta_dict = yaml.load(f, Loader=yaml.FullLoader)
            yml_dict.append(meta_dict)
    df_yml = pd.DataFrame.from_dict(yml_dict)


    # Merge Dataframes on package_id
    df_merged = pd.merge(df_yml,df_profiles['package_id','profile_link','last_modified','source_file','profile_library'],
                         left_on=['package_id'],right_on=['package_id'], how='left')


    # Write merged to markdown
    md_table = df_merged.to_markdown(index=False)
    with open(pvars.md_file, 'w') as f:
        f.write(md_table)

    # Write merged to new YAML file
    df_merged.to_csv(pvars.web_source_csv, index=False, encoding='utf-8')

generate_web_sources(pvars.target_dir, pvars.source_data_dir)


