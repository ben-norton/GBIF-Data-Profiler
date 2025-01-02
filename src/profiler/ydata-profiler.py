from ydata_profiling import ProfileReport
import pandas as pd
from datetime import date
from pathlib import Path
import os
import config as cfg
import yaml

root_dir = cfg.get_project_root()
archive_code = '0052487-241126133413365'
source_filename = 'occurrence.txt'

today = date.today()
ts = today.strftime("%Y%m%d")

# Paths
current_path = Path().absolute()
root_path = current_path.parent.parent
source_path = str(root_path) + '/source-data/' + archive_code + '/'

# Metadata
meta_yaml = str(source_path) + '/meta.yml'
with open(meta_yaml, 'r') as f:
    meta = yaml.safe_load(f)

# Load file (CSV should be automatically identified)
source_file = str(source_path) + '/' + source_filename

# Target Files
target_path = str(current_path) + '/output/'
if not os.path.isdir(target_path):
    os.mkdir(target_path)
target_report = str(target_path) + '/' + archive_code + '-' + str(ts) + '-output.html'

df = pd.read_csv(source_file, sep='\t', lineterminator='\n', on_bad_lines='skip')
title = archive_code + ' Occurrence Data Profile'
ydata_config_file = str(current_path) + '/configs/nmnh_gbif_config_minimal.yaml'

if 'title' in meta.keys():
    title = meta['title']
else:
    title = archive_code
if 'doi' in meta.keys():
    doi = meta['doi']
else:
    doi = None

dataset_dict = {
    "description": title,
    "url": doi
}

profile = ProfileReport(df,
                        title=title,
                        dataset=dataset_dict,
                        minimal=True
                        )
profile.to_file(target_report)