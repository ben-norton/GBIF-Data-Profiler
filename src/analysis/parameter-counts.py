import pandas as pd
import config as cfg
from datetime import date
import os

today = date.today()
ts = today.strftime("%Y%m%d")

dataset_code = 'all'
datasets = cfg.get_datasets(dataset_code)
root_dir = cfg.get_project_root()
cols = cfg.get_gbif_columns()
col_dtypes = cfg.get_gbif_columns_dtypes()

for dataset in datasets:
    archive_code = dataset
    print(archive_code)
    root_dir = cfg.get_project_root()
    source_file = str(root_dir) + '/source-data/' + archive_code + '/occurrence.txt'
    target_path = str(root_dir) + '/src/analysis/output/parameter-counts/' + str(ts)

    if not os.path.isdir(target_path):
        os.mkdir(target_path)

    # Create file contain unique value counts where more than one unique values
    unique_counts_file = str(target_path) + '/' + archive_code + '-unique-counts.txt'
    # Create file containing columns with unique and non-null counts and detected dtype
    column_profile_file = str(target_path) + '/' + archive_code + '-column-profiles.txt'
    # Create template of columns with more than one unique value
    template_file = str(target_path) + '/' + archive_code + '-template.txt'

    #df = pd.read_csv(source_file, sep='\t', lineterminator='\n', on_bad_lines='skip')
    df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8', usecols=cols, low_memory=False)

    # Write Output of Column Profiles
    output = []
    counts = []
    for col in df.columns:
        nonNull = df[col].count()
        unique = df[col].nunique()
        dataType = str(df[col].dtype)
        output.append([col, nonNull, unique, dataType])
        if unique > 1:
            counts.append([col, unique])

    output_df = pd.DataFrame(output)
    output_df.columns = ['column_name','non_null', 'unique_count', 'dtype']
    output_df.to_csv(column_profile_file, index=False)

    unique_counts_df = pd.DataFrame(counts)
    unique_counts_df.columns = ['column_name','unique_count']
    unique_counts_df.to_csv(unique_counts_file, index=False)

    # Write Template
    template = []
    for col in df.columns:
        unique = df[col].nunique()
        if unique > 1:
            template.append([col])

    template_df = pd.DataFrame(template)
    template_df.columns = ['column_name']
    template_df.to_csv(template_file, index=False)
