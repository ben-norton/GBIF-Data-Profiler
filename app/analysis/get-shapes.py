import pandas as pd
import os
from datetime import date
import globals as cfg
from py_markdown_table.markdown_table import markdown_table

# Get Source Datasets Dataframe Shapes

today = date.today()
ts = today.strftime("%Y%m%d")


source_file_type = 'verbatim'  # Set as needed
dataset_code = 'all'            # Set as needed

root_dir = cfg.get_project_root()
datasets = cfg.get_datasets(dataset_code)
source_filename = source_file_type + '.txt'
md_file = str(root_dir) + '/web/app/md/dataset-shapes-table.md'

shape_dict = {}
for dataset in datasets:
    archive_code = dataset
    print(archive_code)

    source_file = str(root_dir) + '/source-data/' + archive_code + '/' + source_filename
    df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8', encoding_errors='ignore', on_bad_lines='skip', dtype=object)
    shape_dict[archive_code] = df.shape

#print(shape_dict)

df_shapes = pd.DataFrame.from_dict(shape_dict, orient='index', columns=['rows', 'columns'])
df_shapes['dataset'] = source_filename
df_shapes.head().style.format("{:,.0f}")
print(df_shapes)
md = df_shapes.to_markdown()
with open(md_file, 'w') as f:
    f.write(md)

#data = df_shapes.to_dict()

#with open(md_file, 'w') as f:
#    f.write(md)
