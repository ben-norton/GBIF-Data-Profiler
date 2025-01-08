from ydata_profiling import ProfileReport
import pandas as pd
from datetime import date
import os
import config as cfg
import yaml

today = date.today()
ts = today.strftime("%Y%m%d")

datasets = cfg.get_all_datasets()

for dataset in datasets:
    archive_code = dataset
    print(archive_code)
    root_dir = cfg.get_project_root()
    source_filename = 'occurrence.txt'

    # Paths
    source_path = str(root_dir) + '/source-data/' + archive_code
    source_file = str(source_path ) + '/occurrence.txt'
    target_path = str(root_dir) + '/src/profiler/output/ydata/' + str(ts)

    # Metadata
    meta_yaml = str(source_path) + '/meta.yml'
    with open(meta_yaml, 'r') as f:
        meta = yaml.safe_load(f)

    # Load file (CSV should be automatically identified)
    source_file = str(source_path) + '/' + source_filename

    # Target Files
    if not os.path.isdir(target_path):
        os.mkdir(target_path)
    target_report = str(target_path) + '/' + archive_code + '-' + str(ts) + '-output.html'

    df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8')
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