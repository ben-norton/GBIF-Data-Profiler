import pandas as pd
from datetime import date
from pathlib import Path
import config as cfg

root_dir = cfg.get_project_root()
archive_code = '0052487-241126133413365'
source_filename = 'occurrence.txt'

today = date.today()
ts = today.strftime("%Y%m%d")

# Paths
current_path = Path().absolute()
root_path = current_path.parent.parent
source_path = str(root_path) + '/source-data/' + archive_code + '/'
source_file = str(source_path) + '/' + source_filename

df = pd.read_csv(source_file, sep='\t', encoding='utf-8', header=None)
print(df.loc[631633])

#