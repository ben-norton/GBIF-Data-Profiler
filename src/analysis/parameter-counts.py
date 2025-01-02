import pandas as pd
import config as cfg
from datetime import date
import os

root_dir = cfg.get_project_root()
archive_code = '0055081-241126133413365'

today = date.today()
ts = today.strftime("%Y%m%d")

source_file = str(root_dir) + '/source-data/' + archive_code + '/occurrence.txt'
target_path = str(root_dir) + '/src/analysis/output/parameter-counts/' + str(ts)

if not os.path.isdir(target_path):
    os.mkdir(target_path)

target_file = str(target_path) + '/' + archive_code + '-counts.txt'
template_file = str(target_path) + '/' + archive_code + '-template.txt'

#df = pd.read_csv(source_file, sep='\t', lineterminator='\n', on_bad_lines='skip')
df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8', low_memory=False)

# Write Output
output = []
for col in df.columns:
    nonNull = df[col].count()
    unique = df[col].nunique()
    dataType = str(df[col].dtype)
    output.append([col, nonNull, unique, dataType])

output_df = pd.DataFrame(output)
output_df.columns = ['column_name','non_null', 'unique_count', 'dtype']
output_df.to_csv(target_file)

# Write Template
template = []
for col in df.columns:
    unique = df[col].nunique()
    if unique > 0:
        template.append([col])

template_df = pd.DataFrame(template)
template_df.columns = ['column_name']
template_df.to_csv(template_file)
