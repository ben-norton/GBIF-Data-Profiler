import sweetviz as sv
import pandas as pd
from datetime import date
import schemas as sch
import globals as cfg
import yaml

today = date.today()
ts = today.strftime("%Y%m%d")

dataset_code = 'all'
datasets = cfg.get_datasets(dataset_code)
root_dir = cfg.get_project_root()
occurrence_cols = sch.get_gbif_columns()
verbatim_cols = sch.get_verbatim_gbif_columns()

sv_config = str(root_dir) + '/app/profiler/configs/sweetviz_gbif.ini'
sv.config_parser.read(sv_config)

for dataset in datasets:
    archive_code = dataset
    print(archive_code)
    source_filename = 'verbatim.txt'
    source_type = 'verbatim'

    # Paths
    source_path = str(root_dir) + '/source-data/' + archive_code
    source_file = str(source_path) + '/' + source_filename
    # Target
    target_path = str(root_dir) + '/app/profilers/output/verbatim'
    target_report = str(target_path) + '/' + str(ts) + '-' + archive_code + '-' + source_filename + '-' + dataset_code + '-' + source_type + '-sv.html'

    # Metadata
    meta_yaml = str(source_path) + '/meta.yml'
    with open(meta_yaml, 'r') as f:
        meta = yaml.safe_load(f)

    # Load file (CSV should be automatically identified)
    source_file = str(source_path) + '/' + source_filename

    # Use pre-defined columns to eliminate the trailing columns and set to all to object to allow parsing by sweetviz
    if(source_type == 'occurrence'):
        cols = occurrence_cols
    elif(source_type == 'verbatim'):
        cols = verbatim_cols
    else:
        cols = sch.get_gbif_columns()
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

