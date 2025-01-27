import pandas as pd
from datetime import date
from pathlib import Path
import globals as cfg
import schemas as sch

# This file detects column datatype for a specific file.
# Files are selected by package_id (archive_code) and package file name (e.g. occurrence.txt)
# Source: https://gist.github.com/mubbashar/adf2d373d73bf191706778f03757a972

root_dir = cfg.get_project_root()
archive_code = '0054921-241126133413365'
source_filename = 'occurrence.txt'

today = date.today()
ts = today.strftime("%Y%m%d")

# Paths
root_dir = cfg.get_project_root()

source_path = str(root_dir) + '/source-data/' + archive_code + '/'
csv_file_path = str(source_path) + '/' + source_filename

df = pd.read_csv(csv_file_path, sep='\t', lineterminator='\n', encoding='utf-8')

print(df.infer_objects().dtypes)
print(df.dtypes.to_dict())
