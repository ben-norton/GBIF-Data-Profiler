from ydata_profiling import ProfileReport
import pandas as pd
from datetime import date
import os
import schemas as sch
import globals as cfg
import yaml

today = date.today()
ts = today.strftime("%Y%m%d")

dataset_code = 'usnm'
datasets = cfg.get_datasets(dataset_code)
root_dir = cfg.get_project_root()
occurrence_cols = sch.get_gbif_columns()
verbatim_cols = sch.get_verbatim_gbif_columns()

for dataset in datasets:
    archive_code = dataset
    print(archive_code)
    source_filename = 'verbatim.txt'
    source_type = 'verbatim'

    # Paths
    source_path = str(root_dir) + '/source-data/' + archive_code
    source_file = str(source_path) + '/' + source_filename
    target_path = str(root_dir) + '/app/profilers/output'
    target_report = str(target_path) + '/' + str(ts) + '-' + archive_code + '-' + source_type + '-' + dataset_code + '-yd.html'

    # Metadata
    meta_yaml = str(source_path) + '/meta.yml'
    with open(meta_yaml, 'r') as f:
        meta = yaml.safe_load(f)

    if (source_type == 'occurrence'):
        cols = occurrence_cols
    elif (source_type == 'verbatim'):
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