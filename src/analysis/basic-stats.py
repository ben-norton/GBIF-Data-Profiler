import pandas as pd
import config as cfg
import os
from datetime import date

root_dir = cfg.get_project_root()

today = date.today()
ts = today.strftime("%Y%m%d")

archive_code = '0049395-241126133413365'

source_file = str(root_dir) + '/source-data/' + archive_code + '/occurrence.txt'

# Target Folder and File
target_path = str(root_dir) + '/src/analysis/output/parameter-counts/' + str(ts)
if not os.path.isdir(target_path):
    os.mkdir(target_path)
target_file = str(target_path) + '/' + archive_code + '-counts.txt'

#df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8')
#df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8', header=None, low_memory=False)

#print(df.iloc[91970:92000])
#print(df.shape)

with open(source_file, 'r', encoding='utf-8') as temp_f:
    # get No of columns in each line
    col_count = [ len(l.split("\t")) for l in temp_f.readlines() ]

### Generate column names  (names will be 0, 1, 2, ..., maximum columns - 1)
column_names = [i for i in range(0, max(col_count))]

df = pd.read_csv(source_file, sep='\t', lineterminator='\n', encoding='utf-8', header=None, low_memory=False, usecols=column_names)
print(df.shape)