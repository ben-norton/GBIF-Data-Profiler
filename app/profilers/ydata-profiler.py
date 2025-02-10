from ydata_profiling import ProfileReport
import pandas as pd
from datetime import date
import os
import schemas as sch
import globals as cfg
import yaml


# This script generates YData interactive profiles of source datasets
# Datasets are specified by dataset_code (see globals.py) and package filename (without the extension)
# Output is placed in the output directory, which is copied to the flask application using a script under utils
# Sweetviz allows for customized configuration files. The configuration for this project is sweetviz_gbif.ini located under configs

dataset_code = 'usnm'
package_file_stem = 'verbatim'

today = date.today()
ts = today.strftime("%Y%m%d")

datasets = cfg.get_datasets(dataset_code)
root_dir = cfg.get_project_root()
occurrence_cols = sch.get_gbif_columns()
verbatim_cols = sch.get_verbatim_gbif_columns()

for dataset in datasets:
    archive_code = dataset
    print(archive_code)
    source_filename = package_file_stem + '.txt'

    # Paths
    source_path = str(root_dir) + '/source-data/' + archive_code
    source_file = str(source_path) + '/' + source_filename
    target_path = str(root_dir) + '/app/profilers/output'
    target_reportname = archive_code + '-' + package_file_stem + '-' + dataset_code + '-yd.html'
    target_report = str(target_path) + '/' + target_reportname

    # Metadata
    meta_yaml = str(source_path) + '/meta.yml'
    with open(meta_yaml, 'r') as f:
        meta = yaml.safe_load(f)

    if (package_file_stem == 'occurrence'):
        cols = occurrence_cols
    elif (package_file_stem == 'verbatim'):
        cols = verbatim_cols
    else:
        cols = sch.get_gbif_columns()

    df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8', usecols=cols, dtype=object)

    # Drop columnns with no values
    df.dropna(how='all', axis=1, inplace=True)

    if 'title' in meta.keys():
        title = meta['title']
    else:
        title = archive_code
    if 'doi' in meta.keys():
        doi = meta['doi']
    else:
        doi = None

    dataset_dict = {
        "description": title + ' ' + archive_code,
        "url": doi
    }

    profile = ProfileReport(df,
                            title=title,
                            dataset=dataset_dict,
                            minimal=True
                            )
    profile.to_file(target_report)

    log_dict = {}
    log_dict['archive_code'] = archive_code
    log_dict['package_file_stem'] = package_file_stem
    log_dict['dataset_code'] = dataset_code
    log_dict['timestamp'] = ts
    log_dict['target_file'] = target_reportname
    log_dict['profiler'] = 'ydata'

    file = open("profiler_log.yml", "a")
    yaml.dump(log_dict, file)
    file.close()