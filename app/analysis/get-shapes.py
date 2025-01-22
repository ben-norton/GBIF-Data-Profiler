import pandas as pd
import os
from datetime import date
import schemas as sch
import globals as cfg
from py_markdown_table.markdown_table import markdown_table

# Get Source Datasets Dataframe Shapes

today = date.today()
ts = today.strftime("%Y%m%d")


dataset_code = 'new'
datasets = cfg.get_datasets(dataset_code)
md_file = 'dataset_shapes.md'

shape_dict = {}
for dataset in datasets:
    archive_code = dataset
    print(archive_code)
    root_dir = cfg.get_project_root()

    source_file = str(root_dir) + '/source-data/' + archive_code + '/verbatim.txt'
    df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8', encoding_errors='ignore', on_bad_lines='skip', dtype=object)
    shape_dict[archive_code] = df.shape
    #print(df.shape)

df_shapes = pd.DataFrame.from_dict(shape_dict,orient='columns')
data = df_shapes.to_dict()
md = markdown_table(data).get_markdown()
print(df_shapes)
with open(md_file, 'w') as f:
    f.write(md)
