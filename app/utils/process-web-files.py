import os
import re
import datetime
import shutil
import globals as cfg
import pathlib
import pandas as pd
import glob
import yaml

"""
    This script serves two purposes, both associated with the web-based documentation
    1. Copies datasets profiles to web documentation for publication
    2. Generates master yaml file to populate jinja templates
"""

root_dir = cfg.get_project_root()

source_dir = str(root_dir) + '/app/profilers/output'
target_dir = str(root_dir) + '/web/app/static/components/dataset-profiles'
source_data_dir = str(root_dir) + '/source-data'
md_file = str(root_dir) + '/web/app/md/dataset-profiles-table.md'
source_datasets_ymlfile = str(root_dir) + '/web/app/md/source-datasets.yaml'
web_source_csv = str(root_dir) + '/web/app/data/web_source.csv'

# Copy Files
def copy(src, dest):
    for name in os.listdir(src):
        pathname = os.path.join(src, name)
        if os.path.isfile(pathname):
            if name.endswith('.html'):
                shutil.copy2(pathname, dest)
                print(pathname + ' copied')
        else:
            copy(pathname, dest)

#copy(source_dir, target_dir)


def generate_yaml(target):
    # Output yaml file
    output_yaml = str(source_data_dir) + '/source-datasets-meta.yml'
    # Create meta.yml dictionary and dataframe from meta.yml files
    yml_dict = []
    files = glob.glob(target + '/**/meta.yml', recursive=True)
    for ymlfile in files:
        with open(ymlfile, 'r') as f:
            meta_dict = yaml.load(f, Loader=yaml.FullLoader)
            yml_dict.append(meta_dict)

    # Write merged yaml to file
    yaml.dump(yml_dict, output_yaml, default_flow_style=False)
    # meta.yml dataframe
    df_yml = pd.DataFrame.from_dict(yml_dict)

#generate_yaml(source_data_dir)

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
    with open(md_file, 'w') as f:
        f.write(md_table)

    # Write merged to new YAML file
    df_merged.to_csv(web_source_csv, index=False, encoding='utf-8')

generate_web_sources(target_dir, source_data_dir)


