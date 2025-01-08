import pandas as pd
from datetime import date
import os
import config as cfg

today = date.today()
ts = today.strftime("%Y%m%d")

datasets = cfg.get_datasets()
root_dir = cfg.get_project_root()
cols = cfg.get_gbif_columns()
col_dtypes = cfg.get_gbif_columns_dtypes()


archive_code = '0052489-241126133413365'
source_filename = 'occurrence.txt'

# Paths
source_path = str(root_dir) + '/source-data/' + archive_code
source_file = str(source_path) + '/' + source_filename

df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8', names=cols, dtype=col_dtypes)
#df = df.astype(dtype=col_dtypes)

column_names = list(df.columns)
print(column_names)