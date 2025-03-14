import os
import sweetviz as sv
import pandas as pd
from datetime import date
import schemas as sch
import globals as cfg
import yaml
import json

# This script generates Sweetviz interactive profiles of source datasets
# Datasets are specified by dataset_code (see globals.py) and package filename (without the extension)
# Output is placed in the output directory, which is copied to the flask application using a script under utils
# Sweetviz allows for customized configuration files. The configuration for this project is sweetviz_gbif.ini located under configs

# Set Source Files
package_file_stem = 'verbatim'
dataset_code = 'br'

today = date.today()
ts = today.strftime("%Y%m%d")

# Set Paths
datasets = cfg.get_datasets(dataset_code)
root_dir = cfg.get_project_root()

# Set Column Sets
occurrence_cols = sch.get_gbif_columns()
verbatim_cols = sch.get_verbatim_gbif_columns()

# Get Profiler Configuration
sv_config = str(root_dir) + '/app/profilers/configs/sweetviz_gbif.ini'
sv.config_parser.read(sv_config)

for dataset in datasets:
    archive_code = dataset
    print(archive_code)
    source_filename = package_file_stem + '.txt'

    # Source
    source_path = str(root_dir) + '/source-data/' + archive_code
    source_file = str(source_path) + '/' + source_filename
    # Target
    target_path = str(root_dir) + '/app/profilers/output'
    target_file = archive_code + '-' + package_file_stem + '-' + dataset_code + '-sv.html'
    target_report = str(target_path) + '/' + target_file

    # Metadata
    meta_yaml = str(source_path) + '/meta.yml'
    with open(meta_yaml, 'r') as f:
        meta = yaml.safe_load(f)

    # Use pre-defined columns to eliminate the trailing columns and set to all to object to allow parsing by sweetviz
    if(package_file_stem == 'occurrence'):
        cols = occurrence_cols
    elif(package_file_stem == 'verbatim'):
        cols = verbatim_cols
    else:
        cols = sch.get_gbif_columns()
    df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8', usecols=cols, dtype=object, quoting=3)

    # Drop columnns with no values
    df.dropna(how='all', axis=1, inplace=True)

    # Drop gbifID
    feature_config = sv.FeatureConfig(skip="gbifID")

    # Analyze
    profile_report = sv.analyze(
        source=df,
        feat_cfg=feature_config,
        pairwise_analysis='off'
    )

    # Generate Report
    profile_report.show_html(
        filepath=target_report,
        open_browser=False,
        layout='widescreen',
        scale=None)

# Log Process to Profiler Log
    log_dict = {}
    log_dict['archive_code'] = archive_code
    log_dict['package_file_stem'] = package_file_stem
    log_dict['dataset_code'] = dataset_code
    log_dict['timestamp'] = ts
    log_dict['target_file'] = target_file
    log_dict['profiler'] = 'sweetviz'

    file = open("profiler_log.yml", "a")
    yaml.dump(log_dict, file)
    file.close()

