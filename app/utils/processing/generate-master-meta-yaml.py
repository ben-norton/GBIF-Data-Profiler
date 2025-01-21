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


# Generate master metadata yaml file

def generate_yaml(target):
    # Output yaml file
    output_yaml = str(pvars.source_data_dir) + '/source-datasets-meta.yml'
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

generate_yaml(pvars.source_data_dir)