import pandas as pd
from datetime import date
import os
import schemas as sch
import globals as cfg

today = date.today()
ts = today.strftime("%Y%m%d")

dataset_code = 'all'
datasets = cfg.get_datasets(dataset_code)
root_dir = cfg.get_project_root()
cols = sch.get_gbif_columns()


archive_code = '0052489-241126133413365'
source_filename = 'verbatim.txt'

# Paths
source_path = str(root_dir) + '/source-data/' + archive_code
source_file = str(source_path) + '/' + source_filename

df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8', dtype=object, nrows=1)
#df = df.astype(dtype=col_dtypes)

cols = list(df.iloc[1:191])

with open(archive_code + '-verbatim-columns.txt', "w") as output:
    output.write(str(cols))