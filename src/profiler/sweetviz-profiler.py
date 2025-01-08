import sweetviz as sv
import pandas as pd
from datetime import date
import os
import config as cfg
import yaml

today = date.today()
ts = today.strftime("%Y%m%d")

datasets = cfg.get_full_datasets()
root_dir = cfg.get_project_root()
cols = cfg.get_gbif_columns()
col_dtypes = cfg.get_gbif_columns_dtypes()
sv_config = str(root_dir) + '/src/profiler/configs/sweetviz_gbif.ini'
sv.config_parser.read(sv_config)

for dataset in datasets:
    archive_code = dataset
    print(archive_code)
    source_filename = 'occurrence.txt'

    # Paths
    source_path = str(root_dir) + '/source-data/' + archive_code
    source_file = str(source_path) + '/occurrence.txt'
    # Target
    target_path = str(root_dir) + '/src/profiler/output/sweetviz/' + str(ts)
    if not os.path.isdir(target_path):
        os.mkdir(target_path)
    target_report = str(target_path) + '/' + archive_code + '-report.html'

    # Metadata
    meta_yaml = str(source_path) + '/meta.yml'
    with open(meta_yaml, 'r') as f:
        meta = yaml.safe_load(f)

    # Load file (CSV should be automatically identified)
    source_file = str(source_path) + '/' + source_filename

    # Use pre-defined columns to eliminate the trailing columns and set to all to object to allow parsing by sweetviz
    df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8', usecols=cols, dtype=object)

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

