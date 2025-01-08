import sweetviz as sv
import pandas as pd
from datetime import date
import os
import config as cfg
import yaml

today = date.today()
ts = today.strftime("%Y%m%d")

datasets = cfg.get_datasets()
root_dir = cfg.get_project_root()
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
    df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8')
    # Fix datatypes - Sweetviz can't parse mixed data types
    df['day'] = df['day'].astype(str)
    df['recordNumber'] = df['recordNumber'].astype(str)
    df['locationID'] = df['locationID'].astype(str)
    df['georeferencedBy'] = df['georeferencedBy'].astype(str)
    df['identificationVerificationStatus'] = df['identificationVerificationStatus'].astype(str)
    df['identificationRemarks'] = df['identificationRemarks'].astype(str)
    df['parentNameUsage'] = df['parentNameUsage'].astype(str)
    df['hasCoordinate'] = df['hasCoordinate'].astype(str)
    df['kingdomKey'] = pd.to_numeric(df['kingdomKey'], errors='coerce')
    df['phylumKey'] = pd.to_numeric(df['phylumKey'], errors='coerce')
    df['classKey'] = pd.to_numeric(df['classKey'], errors='coerce')
    df['orderKey'] = pd.to_numeric(df['orderKey'], errors='coerce')
    df['familyKey'] = pd.to_numeric(df['familyKey'], errors='coerce')
    df['genusKey'] = pd.to_numeric(df['genusKey'], errors='coerce')
    df['speciesKey'] = pd.to_numeric(df['speciesKey'], errors='coerce')
    df['acceptedNameUsageID'] = df['acceptedNameUsageID'].astype(str)
    df['vernacularName'] = df['vernacularName'].astype(str)
    df['elevation'] = df['elevation'].astype(str)
    df['elevationAccuracy'] = df['elevationAccuracy'].astype(str)
    df['depth'] = df['depth'].astype(str)
    df['distanceFromCentroidInMeters'] = df['distanceFromCentroidInMeters'].astype(str)
    df['acceptedTaxonKey'] = pd.to_numeric(df['acceptedTaxonKey'], errors='coerce')
    df['isSequenced'] = df['isSequenced'].astype(str)
    df['endDayOfYear'] = df['endDayOfYear'].astype(str)
    df['verbatimElevation'] = df['verbatimElevation'].astype(str)
    df['nomenclaturalCode'] = df['nomenclaturalCode'].astype(str)

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

